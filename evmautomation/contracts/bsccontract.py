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

    def get_pcs_token_price(self, token_address: str) -> Decimal: 
        """
        requests USD price for a given token address from
        pancakeswap.
        """

        pcs_data = requests.get(PANCAKESWAP_API_URL_TOKENS + token_address)
        json_data = pcs_data.json()
        price = Decimal(json_data['data']['price'])
        if price > 0:
            return price
        else:
            return False

    def get_pcs_bnb_price(self) -> Decimal:
        """
        requests the current price for the BNB coin.
        """

        return self.get_pcs_token_price(WBNB_TOKEN_ADDRESS)