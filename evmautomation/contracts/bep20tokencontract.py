"""
BEP20 Token Contract Subclass
"""

from decimal import Decimal
from evmautomation.contracts import BscContract
from evmautomation.defines.bsc import BEP20_TOKEN_ABI

class BEP20TokenContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the DRIP Token Contract.
    """

    def __init__(self, rpc_url: str, wallet_address: str, contract_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, contract_address, BEP20_TOKEN_ABI, wallet_address)

    def get_balance_of(self, unit: str = 'wei'):
        return Decimal(self._web3.fromWei(self._contract.functions.balanceOf(self._wallet).call(), unit))

    def get_allowance(self, owner: str, spender: str):
        return self._contract.functions.allowance(owner, spender).call()

    def get_symbol(self):
        return self._contract.functions.symbol().call()