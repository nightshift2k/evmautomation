import logging
import humanize
from datetime import timedelta
from typing import List
from hexbytes import HexBytes
from evmautomation.tools.config import AttrDict
from evmautomation.contracts import DripGardenContract
from evmautomation.workflows import BscWorkflow
from evmautomation.defines.generic import NULL_ADDRESS
from requests.exceptions import RequestException
from evmautomation.tools.config import AttrDict

from pprint import pprint

LOG = logging.getLogger('evmautomation')

class DripGardenWorkflow(BscWorkflow):

    _default_config: AttrDict = {
        "disabled": True,
        "run_every_seconds": 60,
        "wallet_bnb_min_balance": 0.01,
        "max_gas": 250000,
        "plant_threshold": 1,
        "referrer": NULL_ADDRESS,
        "seeds_loss_threshold": 0.003,
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

                # not our time yet
                if not self.need_to_run(address):
                    continue

                contract = DripGardenContract(self.last_rpc_url, address)
                bnb_balance = contract.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                total_plants = contract.get_plants_planted()
                new_plants, seed_remainder = contract.get_plants_ready_and_seed_remainder()
                seeds_loss_pct = (seed_remainder / contract.seeds_per_plant)
                seed_range = True if seeds_loss_pct <= self.config.seeds_loss_threshold else False

                LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - Total Plants = {total_plants}, New Plants = {new_plants}')
                LOG.debug(f'wallet {address} - Unfinished Plant Seeds = {seed_remainder} - Seeds Loss % = {seeds_loss_pct*100:.3f}% - In Planting Range = {seed_range}')

                plant_tx = contract.get_plant_transaction(self.config.referrer, self.config.max_gas)
                plant_fees = contract.estimate_transaction_fees(plant_tx)
                
                if not plant_fees:
                    optimal_gas = contract.estimate_gas_fees(contract.get_plant_transaction(self.config.referrer, 10000000))
                    LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {self.config.max_gas} - optimal gas estimated = {optimal_gas}')
                    self.tg_send_msg(
                        f'*⛽ GAS TOO LOW!*\n\n' \
                        f'*Current Max GAS:* `{self.config.max_gas}`\n' \
                        f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                        f'Try to raise `max_gas` in the config!\n\n' \
                        f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                        address
                    )
                    LOG.debug(f"sleeping for {self.config.run_every_seconds} seconds, in expecation of lower gas")
                    self.set_next_run(address, self.config.run_every_seconds)
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
                            next_run = next_plant_time

                        else:
                            if new_plants >= plants_threshold and not seed_range:
                                LOG.debug(f'wallet {address} - not planting due to Seed Loss {seeds_loss_pct*100:.3f}% > {self.config.seeds_loss_threshold*100:.3f}%')

                            if plants_threshold > new_plants:
                                plants_needed = plants_threshold - new_plants
                            else:
                                plants_needed = 1

                            seeds_needed = contract.get_seeds_needed(plants_needed)
                            next_plant_time = contract.calculate_next_plant(plants_needed)
                            LOG.debug(f'wallet {address} - time to finish required {plants_needed} plant(s) ({seeds_needed} seeds needed) = {humanize.precisedelta(timedelta(seconds=next_plant_time))}')
                            if next_plant_time < self.config.run_every_seconds:
                                next_run = next_plant_time
                            else:
                                next_run = self.config.run_every_seconds
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

            except RequestException as re:
                self.rpc_back_off()
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
                self.set_next_run(address, min(next_run, self.config.run_every_seconds))

        # end for

    def run(self):
        if self.config.disabled == True:
            return

        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        while True:
            # main logic lives inside process_loop()
            self.process_loop()

    def _plant_at(self, plants_owned):
        if isinstance(self.config.plant_table, AttrDict):
            for k,v in self.config.plant_table.items():
                if(plants_owned >= int(k)):
                    break
        if v is not None and v > 0:
            return k, v
        else:
            return 0, self.config.plant_threshold # default 1 plant