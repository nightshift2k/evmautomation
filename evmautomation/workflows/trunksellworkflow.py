from datetime import timedelta
from decimal import Decimal
import logging
import humanize
from time import time
from typing import List
from hexbytes import HexBytes
from evmautomation.defines.bsc import BUSD_TOKEN_ADDRESS
from evmautomation.defines.trunk import TRUNK_TOKEN_CONTRACT_ADDRESS
from evmautomation.contracts import BEP20TokenContract, PancakeSwapRouterContract
from evmautomation.workflows import BscWorkflow
from evmautomation.tools.config import AttrDict
from requests.exceptions import RequestException
from web3 import Web3

LOG = logging.getLogger('evmautomation')

class TrunkSellWorkflow(BscWorkflow):

    _default_config: AttrDict = {
        "disabled": True,
        "run_every_seconds": 86400,
        "wallet_bnb_min_balance": 0.01,
        "pcs_max_gas": 500000,
        "sell_minimum_price": 1,
        "sell_slippage": 0.001,
        "sell_minimum_amount": 100,
        "sell_reserve": 0.01,
        "pcs_transaction_timeout": 120,
        "pcs_collecting_wallet": False,
    }


    def __init__(self, config=None, decryption_key: str = None) -> None:
            merged_config = self._default_config | config 
            super().__init__(merged_config, decryption_key)
            self.load_wallets(self.config.wallet_file)

            self.token_path = [
                TRUNK_TOKEN_CONTRACT_ADDRESS,
                BUSD_TOKEN_ADDRESS
            ]

    def process_loop(self):
        if not (isinstance(self.wallets, List) and len(self.wallets) > 0):
            return False

        for wallet in self.wallets:
            try:
                address, private_key = wallet

                # not our time yet
                if not self.need_to_run(address):
                    continue
              
                self.set_next_run(address, self.config.run_every_seconds)

                # initialize contracts
                pcsrouter = PancakeSwapRouterContract(self.last_rpc_url, address)
                token = BEP20TokenContract(self.last_rpc_url, address, TRUNK_TOKEN_CONTRACT_ADDRESS)

                bnb_balance = pcsrouter.get_balance()
                bnb_min_balance = Decimal(self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0)

                # Fetch token wallet balance
                token_balance = token.get_balance_of('ether')

                if token_balance > 0:
                    if token_balance < self.config.sell_minimum_amount :
                        LOG.debug(f'wallet {address} - token balance of {token_balance:.4f} TRUNK is < than min sell amount of {self.config.sell_minimum_amount:.4f} - skipping!')
                        continue
                    
                    # Fetch values from PCS
                    pcs_busd_value = pcsrouter.get_amounts_out(token_balance, self.token_path)
                    pcs_busd_u_value = pcsrouter.get_amounts_out(1, self.token_path)

                    if pcs_busd_u_value < self.config.sell_minimum_price:
                        LOG.debug(f'wallet {address} - TRUNK/BUSD price = {pcs_busd_u_value:.6f} < minimum price = {self.config.sell_minimum_price:.6f} - skipping!')
                        self.set_next_run(address, 60) # run in 60s again
                        continue
                
                    target_amount_out = pcs_busd_value * Decimal(1 - self.config.sell_slippage)

                    LOG.debug(f'wallet {address} - slippage set to {(self.config.sell_slippage*100):.2f}%')
                    LOG.debug(f'wallet {address} - current unit price (PCS) = {pcs_busd_u_value:.4f} BUSD - minimum amount for {token_balance:.6f} TRUNK = {target_amount_out:.4f} BUSD (max amount = {pcs_busd_value:.4f} BUSD)')

                    if self.config.pcs_collecting_wallet is not None:
                        pcs_collecting_wallet = Web3.toChecksumAddress(self.config.pcs_collecting_wallet)
                        if not Web3.isAddress(pcs_collecting_wallet):
                            pcs_collecting_wallet = Web3.toChecksumAddress(address)
                        else:
                            LOG.debug(f'wallet {address} - sold tokens on PCS will be sent to this address: {pcs_collecting_wallet}')

                    # Fetch BUSD balance for collecting wallet
                    busd = BEP20TokenContract(self.last_rpc_url, pcs_collecting_wallet, BUSD_TOKEN_ADDRESS)
                    busd_balance = busd.get_balance_of('ether')


                    sell_tx = pcsrouter.get_swap_exact_tokens_for_tokens_transaction(
                        token_balance,
                        target_amount_out,
                        self.token_path,
                        pcs_collecting_wallet,
                        int(time() + self.config.pcs_transaction_timeout), 
                        self.config.pcs_max_gas
                    )

                    sell_fees = pcsrouter.estimate_transaction_fees(sell_tx)

                    if not sell_fees:
                        optimal_gas = pcsrouter.estimate_gas_fees(
                            pcsrouter.get_swap_exact_tokens_for_tokens_transaction(
                                token_balance,
                                target_amount_out,
                                self.token_path,
                                pcs_collecting_wallet,
                                int(time() + self.config.pcs_transaction_timeout), 
                                self.config.pcs_max_gas
                            )                        
                        )
                        max_gas = self.config.pcs_max_gas

                        LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {max_gas} - optimal gas estimated = {optimal_gas}')

                        self.tg_send_msg(
                            f'*⛽ GAS TOO LOW FOR SELLING ON PCS!*\n\n' \
                            f'*Current Max GAS:* `{max_gas}`\n' \
                            f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                            f'Try to raise `pcs_max_gas` in the config!\n\n' \
                            f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                            address
                        )
                        continue
                    else:
                        min_balance = max(bnb_min_balance, sell_fees)

                        if bnb_balance < min_balance:
                            LOG.error(f'wallet {address} -  not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                            self.tg_send_msg(
                                f'*❌ Wallet balance too low for hydration!*\n\n' \
                                f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                address
                            )
                        else:
                            tx_receipt = pcsrouter.send_transaction(sell_tx, private_key)
                            
                            # post transaction processing
                            tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                            tx_gas_cost = tx_gas_fees * pcsrouter.get_gas_price()
                            tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                            LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                            self.wait_for_tx_confirmation(tx_hash)

                            new_bnb_balance = pcsrouter.get_balance()
                            new_busd_balance = busd.get_balance_of('ether')
                
                            busd_recieved = new_busd_balance - busd_balance
                            tg_msg = f'*🏧 TRUNK Sell performed!*\n\n' \
                                f'*TRUNK sold:* `{token_balance:.6f} BNB`\n' \
                                f'*BUSD recieved::* `{busd_recieved:.6f} BUSD`\n' \
                                f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                f'*Transaction:* https://bscscan.com/tx/{tx_hash}'

                            self.tg_send_msg(tg_msg, address)

            except RequestException as re:
                self.rpc_back_off()
                self.set_next_run(address, 1)
                LOG.exception(re)
                continue
                
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING HYDRATION!*\n\n' \
                    f'*Error Message:* `{e}`',
                    address
                )
                LOG.exception(e)
                continue
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