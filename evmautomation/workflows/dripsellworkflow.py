from datetime import timedelta
from decimal import Decimal
import logging
from time import time
from typing import List
from hexbytes import HexBytes
from evmautomation.defines.bsc import BUSD_TOKEN_ADDRESS
from evmautomation.defines.drip import DRIP_TOKEN_CONTRACT_ADDRESS
from evmautomation.contracts import (
    BEP20TokenContract, 
    DripTokenContract, 
    DripFaucetContract, 
    DripFountainContract, 
    PancakeSwapRouterContract
)
from evmautomation.tools.config import AttrDict
from evmautomation.workflows import BscWorkflow
from requests.exceptions import RequestException
import humanize
from web3 import Web3

LOG = logging.getLogger('evmautomation')

class DripSellWorkflow(BscWorkflow):
    """
    Subclass for the Drip Sell Workflow

    Sells DRIP when specified conditions apply.
    Can sell on the internal DEX and PancakeSwap
    and also transfer directly the exchanged amount on PancakeSwap
    to another wallet (collection of funds)
    """

    _default_config: AttrDict = {
        "disabled": True,
        "run_every_seconds": 86400,
        "wallet_bnb_min_balance": 0.01,
        "dex_max_gas": 500000,
        "pcs_max_gas": 500000,
        "sell_minimum_price": 10,
        "sell_mode": 0,
        "sell_slippage": 0.001,
        "sell_minimum_amount": 0.5,
        "sell_dex_min_spread": 0.025,
        "pcs_transaction_timeout": 120,
        "pcs_collecting_wallet": False,
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
                address, private_key = wallet

                # not our time yet
                if not self.need_to_run(address):
                    continue
                
                self.set_next_run(address, self.config.run_every_seconds)
               
                # initialize contracts
                faucet = DripFaucetContract(self.last_rpc_url, address)
                fountain = DripFountainContract(self.last_rpc_url, address)
                token = DripTokenContract(self.last_rpc_url, address)
                pcsrouter = PancakeSwapRouterContract(self.last_rpc_url, address)

                # Fetch BNB balance                
                bnb_balance = faucet.get_balance()
                bnb_min_balance = self.config.wallet_bnb_min_balance if self.config.wallet_bnb_min_balance is not None else 0

                # Fetch token wallet balance
                token_balance = token.get_balance_of()

                # get wallet tax stats
                wallet_tax = token.get_tax_rate()
                if token_balance > 0:
                    if token_balance < self.config.sell_minimum_amount :
                        continue

                    # Get internal DEX price and PCS price
                    pcs_wbnb_price = pcsrouter.get_bnb_price()
                    dex_bnb_value = fountain.get_token_to_bnb_input_price(token_balance)
                    dex_value =  dex_bnb_value * pcs_wbnb_price
                    pcs_busd_value = pcsrouter.get_amounts_out(token_balance, [token._contract_address, BUSD_TOKEN_ADDRESS])
                    dex_u_value = fountain.get_token_to_bnb_input_price(1) * pcs_wbnb_price
                    pcs_u_value = pcsrouter.get_amounts_out(1, [token._contract_address, BUSD_TOKEN_ADDRESS])
                    dex_to_pcs_pct = (dex_value / pcs_busd_value) - 1
                    sell_on_dex = dex_to_pcs_pct > Decimal(self.config.sell_dex_min_spread)
                    LOG.debug(f'wallet {address} - BNB = {bnb_balance:.6f} - DRIP balance = {token_balance:.4f}')
                    LOG.debug(f'wallet {address} - DRIP tax tier = {(100*wallet_tax):.0f}%')
                    LOG.debug(f'wallet {address} - current USD value - pre-tax (DEX/PCS) = {dex_value:.4f}/{pcs_busd_value:.4f} | post-tax (DEX/PCS) = {dex_value*(1-wallet_tax):.4f}/{pcs_busd_value*(1-wallet_tax):.4f}')
                    LOG.debug(f'wallet {address} - current unit price (DEX/PCS) = {dex_u_value:.4f}/{pcs_u_value:.4f} | DEX to PCS = {(100*dex_to_pcs_pct):.4f}%')
                    LOG.debug(f'wallet {address} - in dynamic mode sell on FOUNTAIN = {sell_on_dex}')
                    
                    if self.config.pcs_collecting_wallet is not None:
                        pcs_collecting_wallet = Web3.toChecksumAddress(self.config.pcs_collecting_wallet)
                        if not Web3.isAddress(pcs_collecting_wallet):
                            pcs_collecting_wallet = Web3.toChecksumAddress(address)
                        else:
                            LOG.debug(f'wallet {address} - sold tokens on PCS will be sent to this address: {pcs_collecting_wallet}')

                    # Fetch BUSD balance for collecting wallet
                    busd = BEP20TokenContract(self.last_rpc_url, pcs_collecting_wallet, BUSD_TOKEN_ADDRESS)
                    busd_balance = busd.get_balance_of('ether')

                    if (dex_u_value < self.config.sell_minimum_price) and (pcs_u_value < self.config.sell_minimum_price):
                        LOG.debug(f'wallet {address} - minimum price of {self.config.sell_minimum_price:.4f} not reached on any DEX! - skipping!')
                        self.set_next_run(address, 60)
                        continue

                    min_price_reached = False
                    current_sell_mode = 0

                    if ( (self.config.sell_mode == 1) or (self.config.sell_mode == 0 and sell_on_dex == True) ) and dex_u_value > self.config.sell_minimum_price:
                        min_price_reached = True
                        current_sell_mode = 1
                        sell_where = "FOUNTAIN"
                        target_token = "BNB"
                        target_amount = dex_bnb_value * (1 - wallet_tax) # deduct tax
                        target_amount = target_amount * Decimal(1 - self.config.sell_slippage)

                        sell_tx = fountain.get_sell_transaction(token_balance, target_amount, self.config.dex_max_gas)
                        sell_fees = fountain.estimate_transaction_fees(sell_tx)

                    elif ( (self.config.sell_mode == 2) or (self.config.sell_mode == 0 and sell_on_dex == False) ) and pcs_u_value > self.config.sell_minimum_price:
                        min_price_reached = True
                        current_sell_mode = 2
                        sell_where = "PCS"
                        target_token = "BUSD"
                        target_amount = pcs_busd_value * (1 - wallet_tax) # deduct tax
                        target_amount = target_amount * Decimal(1 - self.config.sell_slippage)

                        sell_tx = pcsrouter.get_swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens_transaction(
                            token_balance,
                            target_amount,
                            [DRIP_TOKEN_CONTRACT_ADDRESS, BUSD_TOKEN_ADDRESS],
                            pcs_collecting_wallet,
                            int(time() + self.config.pcs_transaction_timeout), 
                            self.config.pcs_max_gas
                        )
                        sell_fees = pcsrouter.estimate_transaction_fees(sell_tx)

                    if not min_price_reached:
                        LOG.debug(f'wallet {address} - minimum token price of {self.config.sell_minimum_price:.4f} not reached on any dex!')
                        continue

                    if current_sell_mode > 0:
                        LOG.debug(f'wallet {address} - sell mode = {current_sell_mode} (1 = Fountain, 2 = PCS) - sell fees estd. = {sell_fees:.6f}')

                        if not sell_fees:
                            if current_sell_mode == 1: # selling on dex
                                optimal_gas = fountain.estimate_gas_fees(fountain.get_sell_transaction(token_balance, target_amount, 10000000))
                                max_gas = self.config.dex_max_gas
                            elif current_sell_mode == 2: # pcs sell
                                # todo implement
                                optimal_gas = pcsrouter.estimate_gas_fees(
                                    pcsrouter.get_swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens_transaction(
                                        token_balance,
                                        target_amount,
                                        [DRIP_TOKEN_CONTRACT_ADDRESS, BUSD_TOKEN_ADDRESS],
                                        pcs_collecting_wallet,
                                        int(time() + self.config.pcs_transaction_timeout), 
                                        10000000
                                    )
                                )
                                max_gas = self.config.pcs_max_gas
                           
                            LOG.warning(f'wallet {address} - gas fee estimation failed - current max gas = {max_gas} - optimal gas estimated = {optimal_gas}')
                           
                            self.tg_send_msg(
                                f'*⛽ GAS TOO LOW FOR SELL ON {sell_where}!*\n\n' \
                                f'*Current Max GAS:* `{max_gas}`\n' \
                                f'*Optimal GAS (estd.):* `{optimal_gas}`\n\n' \
                                f'Try to raise `dex_max_gas/pcs_max_gas` in the config!\n\n' \
                                f'Will wait `{humanize.precisedelta(timedelta(seconds=self.config.run_every_seconds))}` for lower gas fees!',
                                address
                            )
                            continue
         
                        # enough BNB for gas...?
                       
                        min_balance = max(bnb_min_balance, sell_fees)
                        if bnb_balance >= min_balance:
                            LOG.debug(f'wallet {address} - trying to sell {token_balance:.4f} DRIP for {target_amount:.6f} {target_token} after {wallet_tax*100}% TAX and {self.config.sell_slippage*100}% slippage')

                            # doesn't matter which contract sends the tx ...
                            tx_receipt = pcsrouter.send_transaction(sell_tx, private_key)
                            # post transaction processing
                            tx_gas_fees = tx_receipt.gasUsed if tx_receipt.gasUsed is not None else 0
                            tx_gas_cost = tx_gas_fees * pcsrouter.get_gas_price()
                            tx_hash = tx_receipt.transactionHash.hex() if (tx_receipt.transactionHash is not None and isinstance(tx_receipt.transactionHash, HexBytes)) else "UNKNOWN"
                            LOG.info(f'wallet {address} - transaction executed, tx hash = {tx_hash}')
                            self.wait_for_tx_confirmation(tx_hash)

                            new_bnb_balance = token.get_balance()
                            new_busd_balance = busd.get_balance_of('ether')

                            # send telegram
                            if current_sell_mode == 1:
                                bnb_recieved = new_bnb_balance - bnb_balance
                                tg_msg = f'*🏧 Sell on {sell_where} performed!*\n\n' \
                                    f'*DRIP sold:* `{token_balance:.6f} DRIP`\n' \
                                    f'*BNB recieved:* `{bnb_recieved:.6f} BNB`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}'
                            elif current_sell_mode == 2:
                                busd_recieved = new_busd_balance - busd_balance
                                tg_msg = f'*🏧 Sell on {sell_where} performed!*\n\n' \
                                    f'*DRIP sold:* `{token_balance:.6f} DRIP`\n' \
                                    f'*BUSD recieved:* `{busd_recieved:.6f} BUSD`\n' \
                                    f'*BUSD wallet:* `{pcs_collecting_wallet}`\n' \
                                    f'*BNB balance:* `{new_bnb_balance:.6f} BNB`\n' \
                                    f'*Gas used:* `{tx_gas_cost:.6f} BNB`\n' \
                                    f'*Transaction:* https://bscscan.com/tx/{tx_hash}'

                            self.tg_send_msg(tg_msg, address)

                        else:
                            LOG.error(f'wallet {address} -  not enough balance, minimum required = {min_balance:.6f} BNB, skipping...')
                            self.tg_send_msg(
                                f'*❌ Wallet balance too low for selling!*\n\n' \
                                f'*Balance:* `{bnb_balance:.6f} BNB`\n' \
                                f'*Minimum:* `{min_balance:.6f} BNB`\n' \
                                f'*Missing:* `{min_balance-bnb_balance:.6f} BNB`',
                                address
                            )
                        # end if bnb_balance >= min_balance
                
            except RequestException as re:
                self.rpc_back_off()
                self.set_next_run(address, 1)
                LOG.exception(re)
                continue
                
            except Exception as e:
                self.tg_send_msg(
                    f'*💀 ERROR WHILE EXECUTING DRIP FAUCET HYDRATE/CLAIM!*\n\n' \
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
            self.process_loop()
            self.sleep_between_loops()
