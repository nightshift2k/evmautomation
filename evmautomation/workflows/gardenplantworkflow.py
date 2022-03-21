import logging
import humanize
from datetime import timedelta
from math import floor
from pprint import pprint
from time import sleep
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import DripGardenContract
from evmautomation.workflows import BscWorkflow
from evmautomation.defines.generic import NULL_ADDRESS

LOG = logging.getLogger('evmautomation')

class GardenPlantWorkflow(BscWorkflow):

    DEFAULT_PLANT_THRESHOLD = 1 # plant at 1 plant
    DEFAULT_SLEEP_LOOP_SECONDS = 30
    DEFAULT_SEEDS_LOSS_THRESHOLD = 0.003

    def __init__(self, config=None, decryption_key: str = None) -> None:
            super().__init__(config, decryption_key)
            self.load_wallets(config.garden.wallet_file)

    def run(self):
        if self.config.garden.disabled == True:
            return

        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        sleep_loop_seconds = self.config.garden.sleep_time if (self.config.garden.sleep_time is not None and self.config.garden.sleep_time >0) else self.DEFAULT_SLEEP_LOOP_SECONDS
        referrer = NULL_ADDRESS if self.config.garden.referrer is not None else self.config.garden.referrer
        seeds_loss_threshold = self.config.garden.max_seeds_loss if self.config.garden.max_seeds_loss is not None and self.config.garden.max_seeds_loss > 0 else self.DEFAULT_SEEDS_LOSS_THRESHOLD
        LOG.debug(f'run garden workflow - referrer = {referrer} - sleep time = {sleep_loop_seconds}s - Seed Loss % Threshold = {seeds_loss_threshold*100:.3f}%')

        while True:
            planting_times = []
            for wallet in self.wallets:
                address, private_key = wallet
                contract = DripGardenContract(self.bsc_rpc_url, address)
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.garden.wallet_bnb_min_balance if self.config.garden.wallet_bnb_min_balance is not None else 0

                total_plants = contract.get_plants_planted()
                seeds = contract.get_user_seeds()
                new_plants, seed_remainder = contract.get_plants_ready_and_seed_remainder()
                # calculate % of seeds lost 
                seeds_loss_pct = (seed_remainder / contract.seeds_per_plant)
                seed_range = True if seeds_loss_pct <= seeds_loss_threshold else False
                LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - Total Plants = {total_plants}, New Plants = {new_plants}')
                LOG.debug(f'wallet {address} - Unfinished Plant Seeds = {seed_remainder} - Seeds Loss % = {seeds_loss_pct*100:.3f}% - In Planting Range = {seed_range}')
                plant_tx = contract.get_plant_transaction(referrer)
                plant_fees = contract.estimate_transaction_fees(plant_tx)
                min_balance = max(bnb_min_balance, plant_fees)
                if bnb_balance >= min_balance:
                    if total_plants > 0:
                        _, plants_threshold = self._plant_at(total_plants)
                        if new_plants >= plants_threshold and seed_range:
                            LOG.info(f'wallet {address} - due for planting at {new_plants} Plants, threshold is >= {plants_threshold} Plants')

                            try:
                                tx_receipt = contract.send_transaction(plant_tx, private_key)
                                tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                                tx_gas_cost = tx_gas_fees * contract.get_gas_price()
                                tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                                ##
                                pprint(tx_receipt)
                                print("tx_hash: ", tx_hash)
                                print("tx_gas_fees: ", tx_gas_fees)
                                ##
                                LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
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

                                LOG.info(f'{wallet} - old amount = {total_plants} - new amount = {new_total_plants} - added = {new_plants}')
                                LOG.info(f'{wallet} - transaction gas = {tx_gas_cost} - BNB balance = {new_bnb_balance}')
                                LOG.info(f'{wallet} - next planting in {humanize.precisedelta(timedelta(seconds=next_plant_time))}')

                                planting_times.append(next_plant_time)
                               
                            except Exception as e:
                                self.tg_send_msg(
                                    f'*💀 ERROR WHILE EXECUTING PLANTING!*\n\n' \
                                    f'*Error Message:* `{e}`',
                                    address
                                )
                                LOG.error(f'wallet {address} - error during plant() transaction: {e}')

                        else:
                            if new_plants >= plants_threshold and not seed_range:
                                LOG.debug(f'wallet {address} - not planting due to Seed Loss {seeds_loss_pct*100:.3f}% > {seeds_loss_threshold*100:.3f}%')

                            if plants_threshold > new_plants:
                                plants_needed = plants_threshold - new_plants
                            else:
                                plants_needed = 1

                            seeds_needed = contract.get_seeds_needed(plants_needed)
                            next_plant_time = contract.calculate_next_plant(plants_needed)
                            LOG.debug(f'wallet {address} - time to finish required {plants_needed} plant(s) ({seeds_needed} seeds needed) = {humanize.precisedelta(timedelta(seconds=next_plant_time))}')
                            planting_times.append(next_plant_time)
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

            if len(planting_times) > 0:
                planting_times.sort()
                next_run = planting_times[0]
            else:
                next_run = self.config.garden.run_every_seconds if self.config.garden.run_every_seconds is not None else 30
            
            sleep_time = min(max(next_run,0), sleep_loop_seconds)
            LOG.debug(f"sleeping for {sleep_time} seconds")
            sleep(sleep_time)

    def _plant_at(self, plants_owned):
        if isinstance(self.config.garden.plant_table, AttrDict):
            for k,v in self.config.garden.plant_table.items():
                if(plants_owned >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.DEFAULT_PLANT_THRESHOLD # default 1 plant