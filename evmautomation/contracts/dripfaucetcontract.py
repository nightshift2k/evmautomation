"""
DRIP Faucet Contract Subclass
"""

from evmautomation.contracts import BscContract
from evmautomation.defines.drip import DRIP_FAUCET_CONTRACT_ADDRESS, DRIP_FAUCET_ABI

class DripFaucetContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the DRIP Faucet Contract.
    """

    DAILY_INTEREST = 0.01 # daily interest rate = 1%

    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, DRIP_FAUCET_CONTRACT_ADDRESS, DRIP_FAUCET_ABI, wallet_address)

    def get_user_info_totals(self):
        """
        calls userInfoTotals() on the contract.
        """

        return self._contract.functions.userInfoTotals(self._wallet).call()

    def get_user_deposits(self):
        """
        get wallets deposits, returns divided by 1e18
        """

        deposits = self._web3.fromWei(self.get_user_info_totals()[1], 'ether')
        return float(deposits)

    def get_user_available(self):
        """
        calls claimsAvailable() on contract,
        returns value divided by 1e18.
        """
        
        available = self._web3.fromWei(self._contract.functions.claimsAvailable(self._wallet).call(), 'ether')
        return float(available)

    def get_user_percent_available(self):
        """
        returns claims available as the percentage
        of the total deposits.
        """

        d = self.get_user_deposits()
        a = self.get_user_available()

        if a > 0:
            return (a / d * 100)
        else:
            return 0

    def get_roll_transaction(self, gas=600000):
        """
        returns the roll transaction.
        """

        tx = self._contract.functions.roll().buildTransaction(self.get_transaction_options(gas))
        return tx

    def calc_time_until_amount_available(self, percent_reach) -> int:
        """
        calculates the time in seconds, when
        available claims reach a given percentage
        of the total deposits.
        """
        
        d = self.get_user_deposits()
        a = self.get_user_available()
        if (d == 0):
            return False
        hydrate_target =  (d * percent_reach)
        missing = max(0, hydrate_target - a)
        per_minute = d * self.DAILY_INTEREST / 86400
        left = int(missing / per_minute)
        return left