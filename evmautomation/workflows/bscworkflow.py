import logging
from time import sleep
from evmautomation.workflows import BaseWorkflow

LOG = logging.getLogger('evmautomation')

class BscWorkflow(BaseWorkflow):

    DEFAULT_BSC_RPC_URL = "https://bsc-dataseed1.defibit.io/"
    DEFAULT_BSC_WAIT_FOR_TX = 60

    def __init__(self, config=None, decryption_key: str = None) -> None:
        super().__init__(config, decryption_key)
        self.bsc_rpc_url = config.bsc.rpc_url if config.bsc.rpc_url is not None else self.DEFAULT_BSC_RPC_URL
        self.bsc_wait_for_tx = config.bsc.wait_for_tx if config.bsc.wait_for_tx is not None else self.DEFAULT_BSC_WAIT_FOR_TX
        LOG.debug(f'BSC url set to {self.bsc_rpc_url}')
        LOG.debug(f'BSC transaction wait time is {self.bsc_wait_for_tx}s')

    def wait_for_tx_confirmation(self, tx_hash=None):
        msg = f'waiting {self.bsc_wait_for_tx}s for transaction'
        msg += f' {tx_hash}' if tx_hash else ''
        msg += ' confirmation'
        LOG.debug(msg)
        sleep(self.bsc_wait_for_tx)