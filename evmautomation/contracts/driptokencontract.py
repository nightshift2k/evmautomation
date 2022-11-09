"""
DRIP Token Contract Subclass
"""

from decimal import Decimal
from evmautomation.contracts import BscContract
from evmautomation.defines.drip import DRIP_TOKEN_CONTRACT_ADDRESS, DRIP_TOKEN_ABI

class DripTokenContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the DRIP Token Contract.
    """

    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, DRIP_TOKEN_CONTRACT_ADDRESS, DRIP_TOKEN_ABI, wallet_address)

    def get_balance_of(self):
        return Decimal(self._web3.fromWei(self._contract.functions.balanceOf(self._wallet).call(), "ether"))

    def get_tax_rate(self):
        _, tax = self._contract.functions.calculateTransferTaxes(self._wallet, self._web3.toWei(1, 'ether')).call()
        return self._web3.fromWei(tax, 'ether')

    # def get_pcs_drip_price(self):
    #     """
    #     return DRIP price in BUSD
    #     """

    #     price, _ = self.get_pcs_token_price(DRIP_TOKEN_CONTRACT_ADDRESS)

    #     return price
