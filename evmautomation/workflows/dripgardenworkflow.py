import logging
import humanize
from datetime import timedelta
from time import sleep
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import DripGardenContract
from evmautomation.workflows import BscWorkflow
from evmautomation.defines.generic import NULL_ADDRESS

LOG = logging.getLogger('evmautomation')

class DripGardenWorkflow(BscWorkflow):

    DEFAULT_MAX_GAS = 250000
    DEFAULT_PLANT_THRESHOLD = 1 # plant at 1 plant
    DEFAULT_SLEEP_LOOP_SECONDS = 30
    DEFAULT_SEEDS_LOSS_THRESHOLD = 0.003
    DEFAULT_RUN_EVERY_SECONDS = 60

    def __init__(self, config=None, decryption_key: str = None) -> None:
            super().__init__(config, decryption_key)
            self.load_wallets(self.config.wallet_file)
            self.max_gas = self.config.max_gas if self.config.max_gas is not None else self.DEFAULT_MAX_GAS
            self.run_every_seconds = self.config.run_every_seconds if self.config.run_every_seconds is not None else self.DEFAULT_RUN_EVERY_SECONDS
            self.sleep_loop_seconds = self.config.sleep_time if (self.config.sleep_time is not None and self.config.sleep_time >0) else self.DEFAULT_SLEEP_LOOP_SECONDS
            self.referrer = NULL_ADDRESS if self.config.referrer is not None else self.config.referrer
            self.seeds_loss_threshold = self.config.max_seeds_loss if self.config.max_seeds_loss is not None and self.config.max_seeds_loss > 0 else self.DEFAULT_SEEDS_LOSS_THRESHOLD

    def process_loop(self):
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False
        next_runs = []
        for wallet in self.wallets:
            try:
                address, private_key = wallet
                contract = DripGardenContract(self.last_rpc_url, address)
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                total_plants = contract.get_plants_planted()
                new_plants, seed_remainder = contract.get_plants_ready_and_seed_remainder()
                seeds_loss_pct = (seed_remainder / contract.seeds_per_plant)
                seed_range = True if seeds_loss_pct <= self.seeds_loss_threshold else False

                LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - Total Plants = {total_plants}, New Plants = {new_plants}')
                LOG.debug(f'wallet {address} - Unfinished Plant Seeds = {seed_remainder} - Seeds Loss % = {seeds_loss_pct*100:.3f}% - In Planting Range = {seed_range}')

                plant_tx = contract.get_plant_transaction(self.referrer, self.max_gas)
                plant_fees = contract.estimate_transaction_fees(plant_tx)
                
                if not plant_fees:
                    optimal_gas = contract.estimate_gas_fees(contract.get_plant_transaction(self.referrer, 10000000))
                    LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.max_gas} - optimal gas estimated = {optimal_gas}')
                    self.tg_send_msg(
                        f'*⛽ GAS TOO LOW!*\n\n' \
                        f'*Current Max GAS:* `{self.max_gas}`\n' \
                        f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                        f'Try to raise `max_gas` in the config!\n\n' \
                        f'Will wait `{humanize.precisedelta(timedelta(seconds=self.run_every_seconds))}` for lower gas fees!',
                        address
                    )
                    LOG.debug(f"sleeping for {self.run_every_seconds} seconds, in expecation of lower gas")
                    next_runs.append(self.run_every_seconds)
                    continue

                min_balance = max(bnb_min_balance, plant_fees)

                if bnb_balance >= min_balance:

                    if total_plants > 0:
                        _, plants_threshold = self._plant_at(total_plants)

                        if new_plants >= plants_threshold and seed_range:
                            LOG.info(f'wallet {address} - due for planting at {new_plants} Plants, threshold is >= {plants_threshold} Plants')
                            tx_receipt = contract.send_transaction(plant_tx, private_key)
                            tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                            tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                            tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                            LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                            self.wait_for_tx_confirmation(tx_hash)
                            
                            new_total_plants = contract.get_plants_planted()
                            _, new_plants_threshold = self._plant_at(new_total_plants)
                            next_plant_time = contract.calculate_next_plant(new_plants_threshold)
                            new_bnb_balance = contract.get_balance()

                            self.tg_send_msg(
                                f'*🌱 Planting performed!*\n\n' \
                                f'*Old Amount:* `{total_plants} Plants`\n' \
                                f'*Current Amount:* `{new_total_plants} Plants`\n' \
                                f'*Added:* `{new_plants} Plants`\n' \
                                f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                f'*Next planting in:* `{humanize.precisedelta(timedelta(seconds=next_plant_time))}`\n' \
                                f'*Transaction:* https://bscscan.com/tx/{tx_hash}',
                                address
                            )

                            LOG.info(f'{address} - old amount = {total_plants} - new amount = {new_total_plants} - added = {new_plants}')
                            LOG.info(f'{address} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                            LOG.info(f'{address} - next planting in {humanize.precisedelta(timedelta(seconds=next_plant_time))}')
                            next_runs.append(next_plant_time)

                        else:
                            if new_plants >= plants_threshold and not seed_range:
                                LOG.debug(f'wallet {address} - not planting due to Seed Loss {seeds_loss_pct*100:.3f}% > {self.seeds_loss_threshold*100:.3f}%')

                            if plants_threshold > new_plants:
                                plants_needed = plants_threshold - new_plants
                            else:
                                plants_needed = 1

                            seeds_needed = contract.get_seeds_needed(plants_needed)
                            next_plant_time = contract.calculate_next_plant(plants_needed)
                            LOG.debug(f'wallet {address} - time to finish required {plants_needed} plant(s) ({seeds_needed} seeds needed) = {humanize.precisedelta(timedelta(seconds=next_plant_time))}')
                            next_runs.append(next_plant_time)
                else:
                    # not enough balance
                    LOG.error(f'wallet {address} has not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                    self.tg_send_msg(
                        f'*❌ Wallet balance to low for planting!*\n\n' \
                        f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                        f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                        f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                        address
                    )
            # end try
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING HYDRATION!*\n\n' \
                    f'*Error Message:* `{e}`',
                    address
                )
                LOG.exception(e)
        # end for

        if len(next_runs) > 0:
            next_runs.sort()
            next_run = next_runs[0]
        else:
            next_run = self.config.run_every_seconds
        
        sleep_time = min(max(next_run,0), self.sleep_loop_seconds)
        return sleep_time

    def run(self):
        if self.config.disabled == True:
            return

        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        LOG.debug(f'run garden workflow - referrer = {self.referrer} - sleep time = {self.sleep_loop_seconds}s - Seed Loss % Threshold = {self.seeds_loss_threshold*100:.3f}%')

        while True:
            self.refresh_rpc_url()
            # main logic lives inside process_loop()
            sleep_time = self.process_loop()
            LOG.debug(f"sleeping for {sleep_time} seconds")
            sleep(sleep_time)

    def _plant_at(self, plants_owned):
        if isinstance(self.config.plant_table, AttrDict):
            for k,v in self.config.plant_table.items():
                if(plants_owned >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.DEFAULT_PLANT_THRESHOLD # default 1 plant