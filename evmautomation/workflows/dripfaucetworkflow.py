from datetime import timedelta
from decimal import Decimal
import logging
import humanize
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import DripTokenContract, DripFaucetContract
from evmautomation.workflows import BscWorkflow
from requests.exceptions import RequestException
from evmautomation.tools.config import AttrDict

LOG = logging.getLogger('evmautomation')

class DripFaucetWorkflow(BscWorkflow):

    _default_config: AttrDict = {
        "disabled": True,
        "run_every_seconds": 86400,
        "wallet_bnb_min_balance": 0.01,
        "hydration_max_gas": 500000,
        "claim_max_gas": 500000,
        "hydrate_threshold": 0.01,
        "hydration_count": 1,
        "claim_threshold": 0.01,
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
                current_hydration_counter = self.pstore[prefix+'current_hydration_counter'] if prefix+'current_hydration_counter' in list(self.pstore.keys()) else 0
                current_claim_counter = self.pstore[prefix+'current_claim_counter'] if prefix+'current_claim_counter' in list(self.pstore.keys()) else 0
                do_hydrate = do_claim = False # set to false for both

                # check if we are in our range of iterations for hydrate and claim
                do_hydrate = current_hydration_counter < self.config.hydration_count and self.config.hydration_count > 0
                do_claim = current_claim_counter < self.config.claim_count and self.config.claim_count > 0

                LOG.debug(f'wallet {address} - do hydrate = {do_hydrate} - do claim = {do_claim}')
                # initialize contracts
                faucet = DripFaucetContract(self.last_rpc_url, address)
                token = DripTokenContract(self.last_rpc_url, address)

                # Fetch BNB balance
                bnb_balance = faucet.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                # Fetch token wallet balance
                token_balance = token.get_balance_of()

                # get Faucet stats for wallet
                deposit = faucet.get_user_deposits()
                available = faucet.get_user_available()
                pct_avail = (available / deposit) if deposit > 0 else 0

                # get wallet tax stats
                wallet_tax = token.get_tax_rate()
                sustainability_fee = faucet.get_sustainability_fee_v2(available)

                LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - DRIP balance = {token_balance:.3f} - DRIP deposits = {deposit:.3f} - DRIP available = {available:.3f} ({pct_avail*100:.2f}%)')
                LOG.debug(f'wallet {address} - DRIP tax tier = {(100*wallet_tax):.0f}% - DRIP whale tax = {sustainability_fee:.0f}%')
                if deposit > 0 and available > 0:
                    _, hydrate_threshold = self._hydrate_at(deposit)
                    _, claim_threshold = self._claim_at(deposit)
                    
                    # we are in the iteration count for hydration
                    if do_hydrate:
                        if pct_avail > hydrate_threshold:
                            hydrate_tx = faucet.get_roll_transaction(self.config.hydration_max_gas)
                            hydrate_fees = faucet.estimate_transaction_fees(hydrate_tx)
                            # if hydrate_fees are None, we tried with too low gas!
                            if not hydrate_fees:
                                optimal_gas = faucet.estimate_gas_fees(faucet.get_roll_transaction(10000000))
                                LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.config.hydration_max_gas} - optimal gas estimated = {optimal_gas}')
                                self.tg_send_msg(
                                    f'*⛽ GAS TOO LOW FOR HYDRATE!*\n\n' \
                                    f'*Current Max GAS:* `{self.config.hydration_max_gas}`\n' \
                                    f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                    f'Try to raise `hydration_max_gas` in the config!\n\n' \
                                    f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                                    address
                                )
                                continue
                            # end if not hydrate_fees
                            min_balance = max(bnb_min_balance, hydrate_fees)
                            LOG.info(f'wallet {address} - due for hydration at {hydrate_threshold*100:.2f}% - threshold is >= {deposit*hydrate_threshold:.3f} DRIP - estimated gas = {hydrate_fees:.6f}')
                            
                            # do we have enough BNB for the transaction?
                            if bnb_balance >= min_balance:
                                # danger zone!
                                tx_receipt = faucet.send_transaction(hydrate_tx, private_key)
                                
                                # increase the hydration counter, write to db
                                current_hydration_counter += 1
                                self.pstore[prefix+'current_hydration_counter'] = current_hydration_counter
                                
                                # post transaction processing
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * faucet.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                self.wait_for_tx_confirmation(tx_hash)

                                new_deposit = faucet.get_user_deposits()
                                new_bnb_balance = faucet.get_balance()

                                self.tg_send_msg(
                                    f'*💧 Hydration performed!*\n\n' \
                                    f'*Old Deposit:* `{deposit:.3f} DRIP`\n' \
                                    f'*Current Deposit:* `{new_deposit:.3f} DRIP`\n' \
                                    f'*Added:* `{available:.3f} DRIP`\n' \
                                    f'*Percent Added:* `{pct_avail*100:.2f}%`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )
                            
                                LOG.info(f'{address} - old deposit = {deposit} DRIP - new deposit = {new_deposit} DRIP - added = {available} DRIP')
                                LOG.info(f'{address} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                                LOG.info(f'{address} - hydration count = {current_hydration_counter} - max hydration count = {self.config.hydration_count}')
                            else:
                                LOG.error(f'wallet {address} -  not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                                self.tg_send_msg(
                                    f'*❌ Wallet balance too low for hydration!*\n\n' \
                                    f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                    f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                    f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                    address
                                )
                            # end if bnb_balance >= min_balance
                        else:
                            time_left = faucet.calc_time_until_amount_available(hydrate_threshold)
                            next_run = time_left
                            LOG.info(f'wallet {address} - available of {deposit*hydrate_threshold:.6f} DRIP ({hydrate_threshold*100:.2f}%) for hydration not reached!')
                            LOG.info(f'wallet {address} - next hydration should approx. occur in {humanize.precisedelta(timedelta(seconds=time_left))}')
                        # end if pct_avail > hydrate_threshold
                    # if all hydrate iterations have been completed
                    # check if due to claim
                    # as it is an "elif" if both are true, hydrate precedes claim!
                    elif do_claim:
                        if pct_avail > claim_threshold:
                            claim_tx = faucet.get_claim_transaction(self.config.claim_max_gas)
                            claim_fees = faucet.estimate_transaction_fees(claim_tx)
                           
                            # if claim_fees are None, we tried with too low gas!
                            if not claim_fees:
                                optimal_gas = faucet.estimate_gas_fees(faucet.get_claim_transaction(10000000))
                                LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.config.claim_max_gas} - optimal gas estimated = {optimal_gas}')
                                self.tg_send_msg(
                                    f'*⛽ GAS TOO LOW FOR CLAIM!*\n\n' \
                                    f'*Current Max GAS:* `{self.config.hydration_max_gas}`\n' \
                                    f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                    f'Try to raise `claim_max_gas` in the config!\n\n' \
                                    f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                                    address
                                )
                                continue
                            # end if not claim_fees
                            min_balance = max(bnb_min_balance, claim_fees)
                            LOG.info(f'wallet {address} - due for claim at {claim_threshold*100:.2f}% - threshold is >= {deposit*claim_threshold:.3f} DRIP - estimated gas = {claim_fees:.6f}')
                            
                            # do we have enough BNB for the transaction?
                            if bnb_balance >= min_balance:
                                # danger zone!
                                tx_receipt = faucet.send_transaction(claim_tx, private_key)

                                # increase the claim counter, write to db
                                current_claim_counter += 1
                                self.pstore[prefix+'current_claim_counter'] = current_claim_counter
                                
                                # post transaction processing
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * faucet.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                self.wait_for_tx_confirmation(tx_hash)
                               
                                new_token_balance = token.get_balance_of()
                                new_bnb_balance = faucet.get_balance()
                                
                                tokens_added = new_token_balance - token_balance
                                fees = available - tokens_added

                                self.tg_send_msg(
                                    f'*💧 Claim performed!*\n\n' \
                                    f'*Old Balance:* `{token_balance:.3f} DRIP`\n' \
                                    f'*Current Balance:* `{new_token_balance:.3f} DRIP`\n' \
                                    f'*Added:* `{tokens_added:.3f} DRIP`\n' \
                                    f'*Fees:* `{fees:.3f} DRIP`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )
                            
                                LOG.info(f'{address} - old balance = {token_balance:.3f} DRIP - new balance = {new_token_balance:.3f} DRIP - added = {tokens_added:3f} DRIP - fees = {fees:.3f} DRIP')
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
                            time_left = faucet.calc_time_until_amount_available(claim_threshold)
                            next_run = time_left
                            LOG.info(f'wallet {address} - available of {deposit*claim_threshold:.3f} DRIP ({claim_threshold*100:.2f}%) for claiming not reached!')
                            LOG.info(f'wallet {address} - next claim should approx. occur in {humanize.precisedelta(timedelta(seconds=time_left))}')

                            # end if bnb_balance >= min_balance
                        # end if pct_avail > claim_threshold
                    # end hydrate/claim
                # end if deposit > 0 and available > 0
            # end try
            
            except RequestException as re:
                self.rpc_back_off()
                self.set_next_run(address, 1)
                continue
                
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING DRIP FAUCET HYDRATE/CLAIM!*\n\n' \
                    f'*Error Message:* `{e}`',
                    address
                )
                LOG.exception(e)
                continue
            # run stuff if everything went through...
            else:
                LOG.info(f'chc = {current_hydration_counter} | ccc = {current_claim_counter} --- mhc = {self.config.hydration_count} | mcc = {self.config.claim_count}')
                # if we reached the end of both cycles, reset all to 0
                if current_hydration_counter >= self.config.hydration_count and current_claim_counter >= self.config.claim_count:
                    current_hydration_counter = current_claim_counter = 0
                    LOG.info(f'wallet {address} - resetting hydration & claim cycle!')

                self.pstore[prefix+'current_hydration_counter'] = current_hydration_counter
                self.pstore[prefix+'current_claim_counter'] = current_claim_counter

                self.set_next_run(address, min(next_run, self.config.run_every_seconds))
            
            # end except

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

    def _hydrate_at(self, deposit):
        
        if isinstance(self.config.hydration_table, AttrDict):
            for k,v in self.config.hydration_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return Decimal(k), Decimal(v)
        else:
            return Decimal(0), Decimal(self.config.hydrate_threshold) # default 1%

    def _claim_at(self, deposit):
        
        if isinstance(self.config.claim_table, AttrDict):
            for k,v in self.config.claim_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return Decimal(k), Decimal(v)
        else:
            return Decimal(0), Decimal(self.config.claim_threshold) # default 1%