import logging
import humanize
from datetime import timedelta
from time import sleep
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import BankRollNetworkStackContract
from evmautomation.workflows import BscWorkflow

LOG = logging.getLogger('evmautomation')

class TrunkNativeWorkflow(BscWorkflow):

    DEFAULT_MAX_GAS = 500000
    DEFAULT_REINVEST_THRESHOLD = 0.01
    DEFAULT_RUN_EVERY_SECONDS = 3600
    DEFAULT_REINVEST_COUNT = 1 # always hydrate
    DEFAULT_CLAIM_COUNT = 0 # never claim


    def __init__(self, config=None, decryption_key: str = None) -> None:
            super().__init__(config, decryption_key)
            self.load_wallets(self.config.wallet_file)
            self.max_gas = self.config.max_gas if self.config.max_gas is not None else self.DEFAULT_MAX_GAS
            self.run_every_seconds = self.config.run_every_seconds if self.config.run_every_seconds is not None else self.DEFAULT_RUN_EVERY_SECONDS

            self.reinvest_count = self.config.reinvest_count if self.config.reinvest_count is not None else self.DEFAULT_REINVEST_COUNT            
            self.claim_count = self.config.claim_count if self.config.claim_count is not None else self.DEFAULT_CLAIM_COUNT

    def process_loop(self):
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        reinvest_times = []
        for wallet in self.wallets:
            try:
                #start try 
                address, private_key = wallet
                contract = BankRollNetworkStackContract(self.last_rpc_url, address)
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                deposit = contract.get_balance_of()
                available = contract.get_dividends_of()
                pct_avail = (available / deposit) if deposit > 0 else 0
                apr = contract.get_apr()
                LOG.info(f'wallet {address} - BNB = {bnb_balance:.6f} - TRUNK deposits = {deposit:.4f} - TRUNK available = {available:.4f} ({pct_avail*100:.2f}%) - current APR = {apr*100:.3f}%')

                if deposit > 0 and available > 0:
                    
                    _, reinvest_threshold = self._reinvest_at(deposit)
                    
                    if pct_avail > reinvest_threshold:
                        LOG.info(f'wallet {address} - due for reinvest at {pct_avail*100:.2f}%, threshold is >= {deposit*reinvest_threshold:.4f} TRUNK')
                        reinvest_tx = contract.get_reinivest_transaction()
                        reinvest_fees = contract.estimate_transaction_fees(reinvest_tx)

                        if not reinvest_fees:
                            optimal_gas = contract.estimate_gas_fees(contract.get_reinivest_transaction(10000000))
                            LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.max_gas} - optimal gas estimated = {optimal_gas}')
                            self.tg_send_msg(
                                f'*⛽ GAS TOO LOW!*\n\n' \
                                f'*Current Max GAS:* `{self.max_gas}`\n' \
                                f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                f'Try to raise `max_gas` in the config!\n\n' \
                                f'Will wait `{humanize.precisedelta(timedelta(seconds=self.run_every_seconds))}` for lower gas fees!',
                                address
                            )
                            reinvest_times.append(self.run_every_seconds) # soft retry 
                            continue
                        
                        min_balance = max(bnb_min_balance, reinvest_fees)
                        
                        if bnb_balance >= min_balance:
                            try:
                                tx_receipt = contract.send_transaction(reinvest_tx, private_key)
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                
                                self.wait_for_tx_confirmation(tx_hash)

                                new_deposit = deposit + available # todo: re-read from contract call
                                new_bnb_balance = contract.get_balance()
                                _, new_reinvest_threshold = self._reinvest_at(new_deposit)
                                next_reinvest_time = contract.calc_time_until_amount_available(new_reinvest_threshold)
                                
                                self.tg_send_msg(
                                    f'*🐘 Reinvest performed!*\n\n' \
                                    f'*Old Deposit:* `{deposit:.4f} TRUNK`\n' \
                                    f'*Current Deposit:* `{new_deposit:.4f} TRUNK`\n' \
                                    f'*Added:* `{available:.4f} TRUNK`\n' \
                                    f'*Percent Added:* `{pct_avail*100:.2f}%`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Next reinvest in:* `{humanize.precisedelta(timedelta(seconds=next_reinvest_time))}`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )

                                LOG.info(f'{wallet} - old deposit = {deposit:.4f} TRUNK - new deposit = {new_deposit:.4f} TRUNK - added = {available:.4f} TRUNK')
                                LOG.info(f'{wallet} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                                LOG.info(f'{wallet} - next reinvest in {humanize.precisedelta(timedelta(seconds=next_reinvest_time))}')

                                reinvest_times.append(next_reinvest_time)
                            
                            except Exception as e:
                                self.tg_send_msg(
                                    f'*💀 ERROR WHILE EXECUTING PLANTING!*\n\n' \
                                    f'*Error Message:* `{e}`',
                                    address
                                )
                                LOG.exception(e)

                        else:
                            LOG.error(f'wallet {address} - not enough balance! minimum required = {min_balance:.6f} BNB, skipping...')
                            self.tg_send_msg(
                                f'*❌ Wallet balance to low for reinvest!*\n\n' \
                                f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                address
                            )
                    else:
                        next_reinvest_time = contract.calc_time_until_amount_available(reinvest_threshold)
                        LOG.info(f'wallet {address} - available of {deposit*reinvest_threshold:.4f} TRUNK ({reinvest_threshold*100:.2f}%) not reached!')
                        LOG.info(f'wallet {address} - reinvest retry in {humanize.precisedelta(timedelta(seconds=next_reinvest_time))}')
                        reinvest_times.append(next_reinvest_time)
            # end try

            # start except
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING REINVEST!*\n\n' \
                    f'*Error Message:* `{e}`',
                    address
                )
                LOG.exception(e)
            # end except
        # end for loop

        # additional measure, for flucatuating dividends is to 
        # lower the max. sleep to run_every_seconds
        reinvest_times.append(self.run_every_seconds)

        # finally check the shortest wait time and sleep
        if isinstance(reinvest_times, List) and len(reinvest_times) > 0:
            reinvest_times.sort()
            sleep_time = reinvest_times[0]
        else:
            sleep_time = self.run_every_seconds

        return sleep_time


    def run(self):
        if self.config.disabled == True:
            return
        
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False        
        
        while True:
            self.refresh_rpc_url()
            # main logic lives inside process_loop()
            sleep_time = self.process_loop()
            LOG.debug(f"sleeping for {sleep_time} seconds")
            sleep(sleep_time)

    def _reinvest_at(self, deposit):
        if isinstance(self.config.reinvest_table, AttrDict):
            for k,v in self.config.reinvest_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.DEFAULT_REINVEST_THRESHOLD # default 1% > daily