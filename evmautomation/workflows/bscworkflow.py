import logging
from evmautomation.workflows import BaseWorkflow

LOG = logging.getLogger('evmautomation')

class BscWorkflow(BaseWorkflow):

    def __init__(self, config=None, decryption_key: str = None) -> None:
        super().__init__(config, decryption_key)
        self.bsc_rpc_url = config.bsc.rpc_url
        LOG.debug(f'BSC url set to {self.bsc_rpc_url}')
