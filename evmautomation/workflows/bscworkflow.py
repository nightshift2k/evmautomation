from datetime import timedelta
import logging
import random
from time import sleep
import arrow
from typing import List

import humanize
from evmautomation.workflows import BaseWorkflow
LOG = logging.getLogger('evmautomation')

class BscWorkflow(BaseWorkflow):

    DEFAULT_RPC_URLS = [
        "https://bsc-dataseed1.defibit.io/"
        ]
    DEFAULT_WAIT_FOR_TX = 60

    DEFAULT_RPC_REFRESH_INTERVAL = 20 

    last_rpc_url = False
    last_rpc_refresh = False


    def __init__(self, config=None, decryption_key: str = None) -> None:
        super().__init__(config, decryption_key)
        self.rpc_urls = config.bsc.rpc_urls if config.bsc.rpc_urls is not None else self.DEFAULT_RPC_URLS
        self.wait_for_tx = config.bsc.wait_for_tx if config.bsc.wait_for_tx is not None else self.DEFAULT_WAIT_FOR_TX
        self.rpc_refresh_interval = config.bsc.rpc_refresh_interval if config.bsc.rpc_refresh_interval is not None else self.DEFAULT_RPC_REFRESH_INTERVAL
        LOG.debug(f'BSC rpc urls = {self.rpc_urls}')
        LOG.debug(f'BSC transaction wait time is {self.wait_for_tx}s')
        self.refresh_rpc_url()

    def wait_for_tx_confirmation(self, tx_hash=None):
        msg = f'waiting {self.wait_for_tx}s for transaction'
        msg += f' {tx_hash}' if tx_hash else ''
        msg += ' confirmation'
        LOG.debug(msg)
        sleep(self.wait_for_tx)

    def refresh_rpc_url(self) -> str:
        if self.rpc_refresh_interval == 0 or self.rpc_refresh_interval == False:
            self.last_rpc_url = self.rpc_urls[random.randint(0, len(self.rpc_urls)-1)]
            LOG.debug(f'random RPC url chosen from list = {self.last_rpc_url}')
        else:
            if (not self.last_rpc_url) or (not self.last_rpc_refresh) or ( (self.last_rpc_refresh + self.rpc_refresh_interval) < arrow.utcnow().int_timestamp):
                refresh_delta = (arrow.utcnow().int_timestamp - self.last_rpc_refresh)
                LOG.debug(f'time to refresh RPC url, last url = {self.last_rpc_url} last refresh {humanize.precisedelta(timedelta(seconds=refresh_delta))} ago')
                self.last_rpc_url = self.get_fastest_rpc_url(self.rpc_urls)
                self.last_rpc_refresh = arrow.utcnow().int_timestamp
                LOG.debug(f'refreshed RPC url = {self.last_rpc_url}, next refresh in approx. {humanize.precisedelta(timedelta(seconds=self.rpc_refresh_interval))}')
        