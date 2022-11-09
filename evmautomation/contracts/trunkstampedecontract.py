"""
TRUNK Stampede Contract Subclass
"""

from evmautomation.contracts import BscContract
from evmautomation.defines.trunk import TRUNK_STAMPEDE_CONTRACT_ADDRESS, TRUNK_STAMPEDE_ABI

class TrunkStampedeContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the TRUNK Stampede Contract.
    """

    DEPOSITS_DIV = 0.75 # deposits divisor (taken from website source)
    REWARDS_FEE = 0.025 # 2.5% on the rewards
    DAILY_INTEREST = 0.0056 # daily interest rate = 0.56%

    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, TRUNK_STAMPEDE_CONTRACT_ADDRESS, TRUNK_STAMPEDE_ABI, wallet_address)

    def get_user_available(self):
        return float(self._web3.fromWei(self._contract.functions.claimsAvailable(self._wallet).call(), "ether")) * (1 - self.REWARDS_FEE)

    def get_user_deposits(self):
        data = self.get_user_info()
        deposits = self._web3.fromWei(data[1] / self.DEPOSITS_DIV, "ether")
        return float(deposits)

    def get_user_info(self):
        return self._contract.functions.userInfo(self._wallet).call()

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
        per_minute = d * self.get_daily_interest() / 86400
        left = int(missing / per_minute)
        return left

    def get_roll_transaction(self, gas=300000):
        """
        returns the roll transaction.
        """

        tx = self._contract.functions.roll().build_transaction(self.get_transaction_options(gas))
        return tx

    def get_claim_transaction(self, gas=600000):
        """
        returns the claim transaction
        """
        tx = self._contract.functions.claim().build_transaction(self.get_transaction_options(gas))
        return tx

    def get_scale_by_peg(self, apr):
        """
        returns the current APR scaled by peg
        """

        scaled_apr = self._web3.fromWei(self._contract.functions.scaleByPeg(self._web3.toWei(apr, "ether")).call(), "ether")
        return float(scaled_apr)

    def get_daily_interest(self):
        return self.get_scale_by_peg(205) / 365 / 100