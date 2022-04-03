"""
TRUNK Backed Contract Subclass
"""

from evmautomation.contracts import BscContract
from evmautomation.defines.trunk import TRUNK_BACKED_POOL_CONTRACT_ADDRESS, TRUNK_BACKED_POOL_ABI

class TrunkBackedPoolContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the TRUNK Backed Pool Contract.
    """

    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, TRUNK_BACKED_POOL_CONTRACT_ADDRESS, TRUNK_BACKED_POOL_ABI, wallet_address)

    def get_daily_estimate(self, user_tokens: int, token_supply: int):
        return self._contract.functions.dailyEstimate(user_tokens, token_supply).call()
