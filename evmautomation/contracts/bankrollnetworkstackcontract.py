"""
TRUNK Native Staking Contract Subclass (aka BankRollNetworkStack)
"""

from evmautomation.contracts import BscContract
from evmautomation.contracts import TrunkBackedPoolContract
from evmautomation.defines.trunk import TRUNK_NATIVE_STAKING_CONTRACT_ADDRESS, TRUNK_NATIVE_STAKING_ABI

class BankRollNetworkStackContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the TRUNK Native Staking Contract.
    """
    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, TRUNK_NATIVE_STAKING_CONTRACT_ADDRESS, TRUNK_NATIVE_STAKING_ABI, wallet_address)
        
        # add nested TrunkBackedPool contract to access APR/APY calculation
        self.trunkbackedpoolcontract = TrunkBackedPoolContract(rpc_url, wallet_address)


    def get_balance_of(self):
        return float(self._web3.fromWei(self._contract.functions.balanceOf(self._wallet).call(), "ether"))

    def get_dividends_of(self):
        return float(self._web3.fromWei(self._contract.functions.dividendsOf(self._wallet).call(), "ether"))

    def get_total_supply(self):
        return float(self._web3.fromWei(self._contract.functions.totalSupply().call(), "ether"))

    def get_user_percent_available(self):
        """
        returns claims available as the percentage
        of the total deposits.
        """

        d = self.get_balance_of()
        a = self.get_dividends_of()

        if a > 0:
            return (a / d * 100)
        else:
            return 0

    def get_daily_interest(self):
        """
        Daily percentage is dynamic, so we need to calculate it 
        through the Trunk Backed Pool Contract
        """
        b = self._contract.functions.balanceOf(self._wallet).call()
        t = self._contract.functions.totalSupply().call()
        daily_estimate = self.trunkbackedpoolcontract.get_daily_estimate(
            user_tokens=b, 
            token_supply=t
        )
        daily_percentage = daily_estimate / b
        return daily_percentage

    def get_apr(self):
        """
        return APR 
        """
        return self.get_daily_interest() * 365

    def calc_apx(self, periods: int) -> float:
        """
        calculate compounded interest over periods
        """
        apx = ( ( 1 + self.get_daily_interest() ) ** periods ) - 1
        return apx

    def calc_time_until_amount_available(self, percent_reach) -> int:
        """
        calculates the time in seconds, when
        available claims reach a given percentage
        of the total deposits.

        This will not be 100% precise, as daily interest
        fluctuates on the native staking

        """
        
        d = self.get_balance_of()
        a = self.get_dividends_of()
        if (d == 0):
            return False
        reinvest_target =  (d * percent_reach)
        missing = max(0, reinvest_target - a)
        per_minute = d * self.get_daily_interest() / 86400
        left = int(missing / per_minute)
        return left

    def get_reinivest_transaction(self, gas=300000):
        """
        returns the reinvest transaction.
        """

        tx = self._contract.functions.reinvest().buildTransaction(self.get_transaction_options(gas))
        return tx