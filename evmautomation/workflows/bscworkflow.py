import logging
import random
from time import sleep
import arrow

from evmautomation.workflows import BaseWorkflow
from evmautomation.defines.generic import NO_RPC_URL_FOUND_SLEEP_TIME, NO_RPC_URL_FOUND_MESSAGE_TIMEOUT
LOG = logging.getLogger('evmautomation')

class BscWorkflow(BaseWorkflow):

    DEFAULT_RPC_URLS = [
        "https://bsc-dataseed1.defibit.io/"
        ]
    DEFAULT_WAIT_FOR_TX = 60

    last_rpc_url = False
    last_rpc_refresh = False


    def __init__(self, config=None, decryption_key: str = None) -> None:
        super().__init__(config, decryption_key)
        
        self.last_rpc_url = self.cstore['last_rpc_url'] if 'last_rpc_url' in list(self.cstore.keys()) else False
        self.last_rpc_refresh = self.cstore['last_rpc_refresh'] if 'last_rpc_refresh' in list(self.cstore.keys()) else False

        self.rpc_urls = config.bsc.rpc_urls if config.bsc.rpc_urls is not None else self.DEFAULT_RPC_URLS
        self.wait_for_tx = config.bsc.wait_for_tx if config.bsc.wait_for_tx is not None else self.DEFAULT_WAIT_FOR_TX
        LOG.debug(f'BSC rpc urls = {self.rpc_urls}')
        LOG.debug(f'BSC transaction wait time is {self.wait_for_tx}s')
        self.refresh_rpc_url()
        LOG.debug(f'current RPC url = {self.last_rpc_url}')


    def wait_for_tx_confirmation(self, tx_hash=None):
        msg = f'waiting {self.wait_for_tx}s for transaction'
        msg += f' {tx_hash}' if tx_hash else ''
        msg += ' confirmation'
        LOG.debug(msg)
        sleep(self.wait_for_tx)

    def refresh_rpc_url(self, current_is_bad = False) -> str:
        unhealthy_total_time = 0
        if (not self.last_rpc_url) or (not self.last_rpc_refresh) or current_is_bad:
            healthy_urls = False
            
            while True:

                healthy_urls = self.get_healthy_rpc_urls(self.rpc_urls, self.last_rpc_url if current_is_bad else "")
                if len(healthy_urls) > 0:
                    self.last_rpc_url = healthy_urls[random.randint(0, len(healthy_urls)-1)]
                    self.last_rpc_refresh = arrow.utcnow().int_timestamp
                    self.cstore['last_rpc_url'] = self.last_rpc_url
                    self.cstore['last_rpc_refresh'] = self.last_rpc_refresh
                    LOG.debug(f'selected RPC url = {self.last_rpc_url}')
                    break   
                else:
                    LOG.debug('no healthy RPC endpoints found, retrying...')
                    sleep(NO_RPC_URL_FOUND_SLEEP_TIME)
                    unhealthy_total_time += NO_RPC_URL_FOUND_SLEEP_TIME
                    if unhealthy_total_time > NO_RPC_URL_FOUND_MESSAGE_TIMEOUT:
                        unhealthy_total_time = 0
                        rpc_urls_str = '\n'.join(self.rpc_urls)
                        self.tg_send_msg(
                            f'*💀 ALL LISTED RPC URLS ARE FAILING!*\n\n' \
                            f'`{rpc_urls_str}`\n\n' \
                            f'please review your config!'
                        )

    def rpc_back_off(self):
        LOG.debug(f'{self.last_rpc_url} is failing, backing off for a while ...')
        self.random_wait(10,20)
        self.refresh_rpc_url(True)
