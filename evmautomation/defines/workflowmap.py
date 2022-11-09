from typing import Dict
from evmautomation.workflows import DripFaucetWorkflow, DripSellWorkflow, DripGardenWorkflow
from evmautomation.workflows import TrunkStampedeWorkflow, TrunkSellWorkflow
from evmautomation.workflows import BNBSellWorkflow

CONFIG_TO_WORKFLOW_MAP: Dict = {
    'dripfaucet': DripFaucetWorkflow,
    'dripsell': DripSellWorkflow,
    'dripgarden': DripGardenWorkflow,
    'trunkstampede': TrunkStampedeWorkflow,
    'trunksell': TrunkSellWorkflow,
    'bnbsell': BNBSellWorkflow
}