from datetime import timedelta
import logging
import optparse
import humanize
from time import sleep
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import DripFaucetContract
from evmautomation.workflows import BscWorkflow

LOG = logging.getLogger('evmautomation')

class DripHydrationWorkflow(BscWorkflow):

    DEFAULT_MAX_GAS = 500000
    DEFAULT_RUN_EVERY_SECONDS = 3600

    def __init__(self, config=None, decryption_key: str = None) -> None:
            super().__init__(config, decryption_key)
            self.load_wallets(config.drip.wallet_file)
            self.max_gas = self.config.drip.max_gas if self.config.drip.max_gas is not None else self.DEFAULT_MAX_GAS
            self.run_every_seconds = self.config.drip.run_every_seconds if self.config.drip.run_every_seconds is not None else self.DEFAULT_RUN_EVERY_SECONDS

    def run(self):
        if self.config.drip.disabled == True:
            return
        
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        
        while True:

            hydration_times = []
            for wallet in self.wallets:
                address, private_key = wallet
                contract = DripFaucetContract(self.bsc_rpc_url, address)
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.drip.wallet_bnb_min_balance if self.config.drip.wallet_bnb_min_balance is not None else 0

                deposit = contract.get_user_deposits()
                available = contract.get_user_available()
                pct_avail = (available / deposit) if deposit > 0 else 0 
                LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - DRIP deposits = {deposit:.3f} - DRIP available = {available:.3f} ({pct_avail*100:.2f}%)')

                if deposit > 0 and available > 0:
                    _, hydrate_threshold = self._hydrate_at(deposit)
                    
                    if pct_avail > hydrate_threshold:
                        hydrate_tx = contract.get_roll_transaction(self.max_gas)
                        hydrate_fees = contract.estimate_transaction_fees(hydrate_tx)
                        if not hydrate_fees:
                            optimal_gas = contract.estimate_gas_fees(contract.get_roll_transaction(10000000))
                            LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.max_gas} - optimal gas estimated = {optimal_gas}')
                            self.tg_send_msg(
                                f'*⛽ GAS TOO LOW!*\n\n' \
                                f'*Current Max GAS:* `{self.max_gas}`\n' \
                                f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                f'Try to raise `max_gas` in the config!\n\n' \
                                f'Will wait `{humanize.precisedelta(timedelta(seconds=self.run_every_seconds))}` for lower gas fees!',
                                address
                            )
                            hydration_times.append(self.run_every_seconds) # soft retry 
                            continue
                            

                        min_balance = max(bnb_min_balance, hydrate_fees)
                        LOG.info(f'wallet {address} - due for hydration at {hydrate_threshold*100:.2f}% - threshold is >= {deposit*hydrate_threshold:.3f} DRIP - estimated gas = {hydrate_fees:.6f}')
                        
                        if bnb_balance >= min_balance:
                            try:        
                                tx_receipt = contract.send_transaction(hydrate_tx, private_key)
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                                self.wait_for_tx_confirmation(tx_hash)

                                new_deposit = contract.get_user_deposits()
                                new_bnb_balance = contract.get_balance()
                                _, new_hydrate_threshold = self._hydrate_at(new_deposit)
                                next_hydration_time = contract.calc_time_until_amount_available(new_hydrate_threshold)

                                self.tg_send_msg(
                                    f'*💧 Hydration performed!*\n\n' \
                                    f'*Old Deposit:* `{deposit:.6f} DRIP`\n' \
                                    f'*Current Deposit:* `{new_deposit:.6f} DRIP`\n' \
                                    f'*Added:* `{available:.6f} DRIP`\n' \
                                    f'*Percent Added:* `{pct_avail*100:.2f}%`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Next roll in:* `{humanize.precisedelta(timedelta(seconds=next_hydration_time))}`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                    address
                                )
                            
                                LOG.info(f'{wallet} - old deposit = {deposit} DRIP - new deposit = {new_deposit} DRIP - added = {available} DRIP')
                                LOG.info(f'{wallet} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                                LOG.info(f'{wallet} - next roll in {humanize.precisedelta(timedelta(seconds=next_hydration_time))}')

                                hydration_times.append(next_hydration_time)

                                ##
                                ##
                            except Exception as e:
                                self.tg_send_msg(
                                    f'*💀 ERROR WHILE EXECUTING HYDRATION!*\n\n' \
                                    f'*Error Message:* `{e}`',
                                    address
                                )
                                LOG.exception(e)

                        else:
                            LOG.error(f'wallet {address} -  not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                            self.tg_send_msg(
                                f'*❌ Wallet balance too low for hydration!*\n\n' \
                                f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                address
                            )
                    
                    else:
                        next_hydration_time = contract.calc_time_until_amount_available(hydrate_threshold)
                        LOG.info(f'wallet {address} - available of {deposit*hydrate_threshold:.6f} DRIP ({hydrate_threshold*100:.2f}%) not reached!')
                        LOG.info(f'wallet {address} - hydration retry in {humanize.precisedelta(timedelta(seconds=next_hydration_time))}')
                        hydration_times.append(next_hydration_time)
                
            # end for loop

            # finally check the shortest wait time and sleep
            if len(hydration_times) > 0:
                hydration_times.sort()
                sleep_time = hydration_times[0]
            else:
                sleep_time = self.run_every_seconds
            
            LOG.debug(f"sleeping for {sleep_time} seconds")
            sleep(sleep_time)


    def _hydrate_at(self, deposit):
        
        if isinstance(self.config.drip.hydration_table, AttrDict):
            for k,v in self.config.drip.hydration_table.items():
                if(deposit >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, 0.01 # default 1%