"""
DRIP Token Contract Subclass
"""

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
        return float(self._web3.fromWei(self._contract.functions.balanceOf(self._wallet).call(), "ether"))
