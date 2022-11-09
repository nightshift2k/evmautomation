from datetime import timedelta
from decimal import Decimal
import logging
import humanize
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.defines.trunk import TRUNK_TOKEN_CONTRACT_ADDRESS
from evmautomation.contracts import TrunkStampedeContract, BEP20TokenContract
from evmautomation.workflows import BscWorkflow
from requests.exceptions import RequestException

LOG = logging.getLogger('evmautomation')

class TrunkStampedeWorkflow(BscWorkflow):

    _default_config: AttrDict = {
        "disabled": True,
        "run_every_seconds": 86400,
        "wallet_bnb_min_balance": 0.01,
        "roll_max_gas": 500000,
        "claim_max_gas": 500000,
        "roll_threshold": 0.0056,
        "roll_count": 1,
        "claim_threshold": 0.0056,
        "claim_count": 0
    }

    def __init__(self, config=None, decryption_key: str = None) -> None:
            merged_config = self._default_config | config 
            super().__init__(merged_config, decryption_key)
            self.load_wallets(self.config.wallet_file)


    def process_loop(self):
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        for wallet in self.wallets:
            try:
                next_run = self.config.run_every_seconds
                address, private_key = wallet
                prefix = address + "_" # key prefix for persistence storage

                # not our time yet
                if not self.need_to_run(address):
                    continue

                # get persistent data
                current_roll_counter = self.pstore[prefix+'current_roll_counter'] if prefix+'current_roll_counter' in list(self.pstore.keys()) else 0
                current_claim_counter = self.pstore[prefix+'current_claim_counter'] if prefix+'current_claim_counter' in list(self.pstore.keys()) else 0
                do_roll = do_claim = False # set to false for both
                
                # check if we are in our range of iterations for roll and claim
                do_roll = current_roll_counter < self.config.roll_count and self.config.roll_count > 0
                do_claim = current_claim_counter < self.config.claim_count and self.config.claim_count > 0

                LOG.debug(f'wallet {address} - do roll = {do_roll} - do claim = {do_claim}')

                # initialize contracts
                contract = TrunkStampedeContract(self.last_rpc_url, address)
                token = BEP20TokenContract(self.last_rpc_url, address, TRUNK_TOKEN_CONTRACT_ADDRESS)

                # Fetch BNB balance
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                # check daily APR for informational reasons
                daily_apr = contract.get_scale_by_peg(205) / 365
                LOG.info(f'current daily APR = {daily_apr:.3f}%')

                # Fetch token wallet balance
                token_balance = token.get_balance_of('ether')

                deposit = contract.get_user_deposits()
                available = contract.get_user_available()
                pct_avail = (available / deposit) if deposit > 0 else 0 
                LOG.info(f'wallet {address} - BNB = {bnb_balance:.6f} - TRUNK balance = {token_balance:.3f} - TRUNK deposits = {deposit:.3f}, TRUNK available = {available:.3f} ({pct_avail*100:.3f}%)')
                               
                if deposit > 0 and available > 0:
                    
                    _, roll_threshold = self._roll_at(deposit)
                    _, claim_threshold = self._claim_at(deposit)

                    # we are in the iteration count for roll
                    if do_roll:
                        if pct_avail > roll_threshold:
                            roll_tx = contract.get_roll_transaction(self.config.roll_max_gas)
                            roll_fees = contract.estimate_transaction_fees(roll_tx)

                            if not roll_fees:
                                optimal_gas = contract.estimate_gas_fees(contract.get_roll_transaction(10000000))
                                LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.config.roll_max_gas} - optimal gas estimated = {optimal_gas}')
                                self.tg_send_msg(
                                    f'*⛽ GAS TOO LOW!*\n\n' \
                                    f'*Current Max GAS:* `{self.config.roll_max_gas}`\n' \
                                    f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                    f'Try to raise `max_gas` in the config!\n\n' \
                                    f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                                    address
                                )
                                continue

                            min_balance = max(bnb_min_balance, roll_fees)
                            LOG.info(f'wallet {address} - due for roll at {roll_threshold*100:.3f}%, threshold is >= {deposit*roll_threshold:.3f} TRUNK - estimated gas = {roll_fees:.6f}')
                            
                            if bnb_balance >= min_balance:
                                # danger zone!
                                tx_receipt = contract.send_transaction(roll_tx, private_key)

                                # increase the roll counter, write to db
                                current_roll_counter += 1
                                self.pstore[prefix+'current_roll_counter'] = current_roll_counter
                                
                                # post transaction processing
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                self.wait_for_tx_confirmation(tx_hash)

                                new_deposit = deposit + available # todo: re-read from contract call
                                new_bnb_balance = contract.get_balance()
                                
                                self.tg_send_msg(
                                    f'*🐘 Roll performed!*\n\n' \
                                    f'*Old Deposit:* `{deposit:.3f} TRUNK`\n' \
                                    f'*Current Deposit:* `{new_deposit:.3f} TRUNK`\n' \
                                    f'*Added:* `{available:.3f} TRUNK`\n' \
                                    f'*Percent Added:* `{pct_avail*100:.3f}%`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )

                                LOG.info(f'{address} - old deposit = {deposit} TRUNK - new deposit = {new_deposit} TRUNK - added = {available} TRUNK')
                                LOG.info(f'{address} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                                LOG.info(f'{address} - roll count = {current_roll_counter} - max roll count = {self.config.roll_count}')
                            else:
                                LOG.error(f'wallet {address} - not enough balance! minimum required = {min_balance:.6f} BNB, skipping...')
                                self.tg_send_msg(
                                    f'*❌ Wallet balance to low for rolling!*\n\n' \
                                    f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                    f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                    f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                    address
                                )
                        else:
                            time_left = contract.calc_time_until_amount_available(roll_threshold)
                            next_run = time_left
                            LOG.info(f'wallet {address} - available of {deposit*roll_threshold:.3f} TRUNK ({roll_threshold*100:.3f}%) for reinvesting not reached!')
                            LOG.info(f'wallet {address} - next reinvest should approx. occur in {humanize.precisedelta(timedelta(seconds=time_left))}')
                    elif do_claim:
                        if pct_avail > claim_threshold:
                            claim_tx = contract.get_claim_transaction(self.config.claim_max_gas)
                            claim_fees = contract.estimate_transaction_fees(claim_tx)
                           
                            # if claim_fees are None, we tried with too low gas!
                            if not claim_fees:
                                optimal_gas = contract.estimate_gas_fees(contract.get_claim_transaction(10000000))
                                LOG.warning(f'wallet {address} - gas fee is too low! - current max gas = {self.claim_max_gas} - optimal gas estimated = {optimal_gas}')
                                self.tg_send_msg(
                                    f'*⛽ GAS TOO LOW FOR CLAIM!*\n\n' \
                                    f'*Current Max GAS:* `{self.claim_max_gas}`\n' \
                                    f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                    f'Try to raise `claim_max_gas` in the config!\n\n' \
                                    f'Will wait `{humanize.precisedelta(timedelta(seconds=self.run_every_seconds))}` for lower gas fees!',
                                    address
                                )
                                continue
                            # end if not claim_fees
                            min_balance = max(bnb_min_balance, claim_fees)
                            LOG.info(f'wallet {address} - due for claim at {claim_threshold*100:.3f}% - threshold is >= {deposit*claim_threshold:.3f} TRUNK - estimated gas = {claim_fees:.6f}')
                            # do we have enough BNB for the transaction?
                            if bnb_balance >= min_balance:
                                # danger zone!
                                tx_receipt = contract.send_transaction(claim_tx, private_key)

                                # increase the claim counter, write to db
                                current_claim_counter += 1
                                self.pstore[prefix+'current_claim_counter'] = current_claim_counter
                                
                                # post transaction processing
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                self.wait_for_tx_confirmation(tx_hash)
                               
                                new_token_balance = token.get_balance_of('ether')
                                new_bnb_balance = contract.get_balance()
                                
                                tokens_added = new_token_balance - token_balance

                                self.tg_send_msg(
                                    f'*🐘 Claim performed!*\n\n' \
                                    f'*Old Balance:* `{token_balance:.3f} TRUNK`\n' \
                                    f'*Current Balance:* `{new_token_balance:.3f} TRUNK`\n' \
                                    f'*Added:* `{tokens_added:.3f} TRUNK`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )
                            
                                LOG.info(f'{address} - old balance = {token_balance:.3f} TRUNK - new balance = {new_token_balance:.3f} TRUNK - added = {tokens_added:3f} TRUNK')
                                LOG.info(f'{address} - transaction gas = {tx_gas_cost:.6f} - BNB balance = {new_bnb_balance:.6f}')
                                LOG.info(f'{address} - claim count = {current_claim_counter} - max claim count = {self.config.claim_count}')
                            else:
                                LOG.error(f'wallet {address} -  not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                                self.tg_send_msg(
                                    f'*❌ Wallet balance too low for claiming!*\n\n' \
                                    f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                    f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                    f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                    address
                                )
                        else:
                            time_left = contract.calc_time_until_amount_available(claim_threshold)
                            next_run = time_left
                            LOG.info(f'wallet {address} - available of {deposit*claim_threshold:.3f} TRUNK ({claim_threshold*100:.3f}%) for claiming not reached!')
                            LOG.info(f'wallet {address} - next claim should approx. occur in {humanize.precisedelta(timedelta(seconds=time_left))}')

                            # end if bnb_balance >= min_balance
                        # end if pct_avail > claim_threshold
                    # end roll/claim
            # end try

            # start except
            except RequestException as re:
                self.rpc_back_off()
                self.set_next_run(address, 1)
                continue
                
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING HYDRATION!*\n\n' \
                    f'*Error Message:* `{e}`',
                    address
                )
                LOG.exception(e)
                continue
            # run stuff if everything went through...
            else:
                LOG.info(f'crc = {current_roll_counter} | ccc = {current_claim_counter} --- mrc = {self.config.roll_count} | mcc = {self.config.claim_count}')
                # if we reached the end of both cycles, reset all to 0
                if current_roll_counter >= self.config.roll_count and current_claim_counter >= self.config.claim_count:
                    current_roll_counter = current_claim_counter = 0
                    LOG.info(f'wallet {address} - resetting roll & claim cycle!')

                self.pstore[prefix+'current_roll_counter'] = current_roll_counter
                self.pstore[prefix+'current_claim_counter'] = current_claim_counter

                self.set_next_run(address, min(next_run, self.config.run_every_seconds))
        # end for loop

    def run(self):
        if self.config.disabled == True:
            return
        
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False        
        
        while True:
            # main logic lives inside process_loop()
            self.process_loop()
            self.sleep_between_loops()

    def _roll_at(self, deposit):
        if isinstance(self.config.roll_table, AttrDict):
            for k,v in self.config.roll_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.config.roll_threshold # default 0.56% > daily

    def _claim_at(self, deposit):
        
        if isinstance(self.config.claim_table, AttrDict):
            for k,v in self.config.claim_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.config.claim_threshold # default 0.56%