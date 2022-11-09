"""
Binance Smart Chain Web3 Subclass
"""

import requests
from decimal import Decimal
from evmautomation.contracts import BaseContract
from evmautomation.defines.bsc import PANCAKESWAP_API_URL_TOKENS, WBNB_TOKEN_ADDRESS

class BscContract(BaseContract):
    """
    Binance Smartchain Class for Web3 contract interaction on
    the BSC network.
    """

    # def get_pcs_token_price(self, token_address: str): 
    #     """
    #     requests BUSD & WBNB price for a given token address from
    #     pancakeswap.
    #     """

    #     pcs_data = requests.get(PANCAKESWAP_API_URL_TOKENS + token_address)
    #     json_data = pcs_data.json()
    #     busd_price = Decimal(json_data['data']['price'])
    #     bnb_price = Decimal(json_data['data']['price_BNB'])

    #     return busd_price, bnb_price

    # def get_pcs_wbnb_price(self):
    #     """
    #     return WBNB price in BUSD
    #     """

    #     price, _ = self.get_pcs_token_price(WBNB_TOKEN_ADDRESS)

    #     return price
        
        