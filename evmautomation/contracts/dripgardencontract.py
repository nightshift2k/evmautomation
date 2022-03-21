"""
DRIP Garden Contract Subclass
"""

from math import floor
from evmautomation.contracts import BscContract
from evmautomation.defines.drip import DRIP_GARDEN_CONTRACT_ADDRESS, DRIP_GARDEN_ABI
from evmautomation.defines.generic import NULL_ADDRESS

class DripGardenContract(BscContract):
    """
    Subclass for Web3 contract interaction with
    the DRIP Garden Contract.
    """
    
    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, DRIP_GARDEN_CONTRACT_ADDRESS, DRIP_GARDEN_ABI, wallet_address)
        
        # setup the value on init
        self.seeds_per_plant = self.get_seeds_per_plant()

    def get_seeds_per_plant(self):
        return int(self._contract.functions.SEEDS_TO_GROW_1PLANT().call())

    def calculate_seed_to_lp(self, seeds):
        return self._web3.fromWei(self._contract.functions.calculateSeedSell(seeds).call(), "ether")

    def get_time_multiplier(self):
        return self._web3.fromWei(self._contract.functions.currentTimeMultiplier().call(), "gwei")

    def get_garden_balance(self):
        return self._web3.fromWei(self._contract.functions.getBalance().call(), "ether")

    def get_total_seeds(self):
        return self._contract.functions.marketSeeds().call()

    def get_user_seeds(self):
        return self._contract.functions.getUserSeeds(self._wallet).call()

    def get_plants_planted(self):
        return self._contract.functions.hatcheryPlants(self._wallet).call()

    def get_seed_to_lp_ratio(self):
        total_seeds = self.get_user_seeds()
        total_lp = float(self.calculate_seed_to_lp(total_seeds))
        return total_lp *.95 

    def get_plants_ready_and_seed_remainder(self):
        seeds = self.get_user_seeds()
        new_plants = int(floor(seeds / self.seeds_per_plant))
        seed_remainder = int(seeds % self.seeds_per_plant)
        return new_plants, seed_remainder
    
    def get_seeds_needed(self, plant_target):
        _, seed_remainder = self.get_plants_ready_and_seed_remainder()
        seeds_needed = (plant_target * self.seeds_per_plant) - seed_remainder        
        return seeds_needed

    def calculate_next_plant(self, plants_needed):
        seeds = self.get_user_seeds()
        total_plants = self.get_plants_planted()
    
        # each plant generates 1 seed per second
        seeds_per_second = total_plants
        seed_remainder = seeds % self.seeds_per_plant
        seeds_needed = (plants_needed * self.seeds_per_plant) - seed_remainder
    
        time_remaining = seeds_needed / seeds_per_second
        return int(time_remaining)

    def get_plant_transaction(self, referrer, gas=500000):
        """
        returns the plant transaction.
        """
        if not referrer:
            referrer = NULL_ADDRESS

        tx = self._contract.functions.plantSeeds(referrer).buildTransaction(self.get_transaction_options(gas))
        return tx