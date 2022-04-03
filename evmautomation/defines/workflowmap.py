from typing import Dict
from evmautomation.workflows import DripFaucetWorkflow, DripGardenWorkflow
from evmautomation.workflows import TrunkStampedeWorkflow, TrunkNativeWorkflow

CONFIG_TO_WORKFLOW_MAP: Dict = {
    'dripfaucet': DripFaucetWorkflow,
    'dripgarden': DripGardenWorkflow,
    'trunkstampede': TrunkStampedeWorkflow,
    'trunknative': TrunkNativeWorkflow
}