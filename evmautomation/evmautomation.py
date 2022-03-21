import os
import logging
from getpass import getpass
from multiprocessing import Process
from typing import Dict

from evmautomation.tools.config import Config, AttrDict
from evmautomation.tools.log import get_logger
from evmautomation.workflows import DripHydrationWorkflow, GardenPlantWorkflow, StampedeRollWorkflow

LOG = logging.getLogger('evmautomation')

class EVMAutomation(Process):

    config: AttrDict = {}

    def __init__(self, config=None):
        self.config = Config(config)
        self.threads = []
        self._decryptions : Dict = {}

        if not self.config.log.disabled:
            get_logger('evmautomation', self.config.log.filename, self.config.log.level)

        if self.config.log_msg:
            LOG.debug(self.config.log_msg)

        if self.config.drip and self.config.drip.disabled != True:
            self._decryptions['drip'] = getpass(prompt = f'enter decryption key for {self.config.drip.wallet_file}: ')

        if self.config.garden and self.config.garden.disabled != True:
            self._decryptions['garden'] = getpass(prompt = f'enter decryption key for {self.config.garden.wallet_file}: ')

        if self.config.stampede and self.config.stampede.disabled != True:
            self._decryptions['stampede'] = getpass(prompt = f'enter decryption key for {self.config.stampede.wallet_file}: ')


    def run(self):
        if self.config.drip and self.config.drip.disabled != True and 'drip' in self._decryptions:
            LOG.debug('drip workflow enabled')
            self.threads.append(DripHydrationWorkflow(config=self.config, decryption_key=self._decryptions['drip']))
        
        if self.config.garden.disabled != True:
            LOG.debug('garden workflow enabled')
            self.threads.append(GardenPlantWorkflow(config=self.config, decryption_key=self._decryptions['garden']))

        if self.config.stampede.disabled != True:
            LOG.debug('stampede workflow enabled')
            self.threads.append(StampedeRollWorkflow(config=self.config, decryption_key=self._decryptions['stampede']))

        try:
            for t in self.threads:
                t.start()
        except KeyboardInterrupt:
            for t in self.threads:
                t.join()
        except Exception:
            LOG.error("EVMAutomation running on PID %d died due to exception", os.getpid(), exc_info=True)
