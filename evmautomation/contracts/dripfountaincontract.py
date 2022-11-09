"""
DRIP Token Contract Subclass
"""

from decimal import Decimal
from evmautomation.contracts import BscContract
from evmautomation.defines.drip import DRIP_FOUNTAIN_CONTRACT_ADDRESS, DRIP_FOUNTAIN_ABI

class DripFountainContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the DRIP Fountain Contract.
    """

    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, DRIP_FOUNTAIN_CONTRACT_ADDRESS, DRIP_FOUNTAIN_ABI, wallet_address)

    def get_token_to_bnb_input_price(self, tokens_sold):
        bnb_price = self._web3.fromWei(self._contract.functions.getTokenToBnbInputPrice(self._web3.toWei(tokens_sold, 'ether')).call(), 'ether')
        return Decimal(bnb_price)


    def get_sell_transaction(self, tokens_sold, min_bnb, gas=600000):

        wei_tokens_sold = self._web3.toWei(tokens_sold, 'ether')
        wei_min_bnb = self._web3.toWei(min_bnb, 'ether')
        tx = self._contract.functions.tokenToBnbSwapInput(wei_tokens_sold, wei_min_bnb).build_transaction(self.get_transaction_options(gas))

        return tx