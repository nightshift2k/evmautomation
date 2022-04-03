import os
import logging
from getpass import getpass
from multiprocessing import Process
from typing import Dict

from evmautomation.defines.workflowmap import CONFIG_TO_WORKFLOW_MAP
from evmautomation.tools.config import Config, AttrDict
from evmautomation.tools.log import get_logger
from evmautomation.tools.encryption import load_encrypted_wallets

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

        if not self.config.db_file:
            LOG.error(f'you need to specify a database file name via "db_file: file.sqlite" in the config!')
            quit(1)
            
        # decrypt necessary wallets
        wallets = self.gather_wallets()

        # find all workflows to run, and create threads
        for e in self.config.workflows:
            workflow = self.config.workflows[e]
            # workflow is not disabled
            if not workflow.disabled:
                workflow['name'] = e
                # workflow name is empty
                if workflow.workflow is None or len(workflow.workflow) == 0:
                    LOG.error(f'{e} has no configured workflow not configured, you need to define a workflow!')
                    continue
                # workflow is not in the list of available
                if workflow.workflow not in CONFIG_TO_WORKFLOW_MAP:
                    LOG.error(f'{workflow.workflow} is unknown, please use one of those: {str(list(CONFIG_TO_WORKFLOW_MAP.keys()))}')
                    continue

                try:
                    # load wf class from mapping
                    wfclass = CONFIG_TO_WORKFLOW_MAP[workflow['workflow']]
                except Exception as e:
                    LOG.exception(e)

                # if workflow class, and wallets are ok, create thread
                if wfclass and workflow.wallet_file in wallets:
                    if not workflow.chain:
                        LOG.error(f'workflow {e} has no chain defined!')
                        continue
                    elif not self.config.chains[workflow.chain]:
                        LOG.error(f'workflow {e} needs config for chain {workflow.chain} but it is not defined!')
                        continue
                    else:
                        workflow[workflow.chain] = self.config.chains[workflow.chain]

                    if self.config['telegram']:
                        workflow['telegram'] = self.config['telegram']
                    
                    if self.config['db_file']:
                        workflow['db_file'] = self.config['db_file']
                    
                    # add a complete and configured workflow to the thread list
                    self.threads.append(wfclass(config=workflow, decryption_key=wallets[workflow.wallet_file])) 


    def run(self):
        """
        core function to run all workflows when they've
        been set up
        """
        if len(self.threads) > 0:
            LOG.debug(f'starting {len(self.threads)} workflow(s) ...')
            try:
                for t in self.threads:
                    t.start()
            except KeyboardInterrupt:
                for t in self.threads:
                    t.join()
            except Exception:
                LOG.error("EVMAutomation running on PID %d died due to exception", os.getpid(), exc_info=True)
        else:
            LOG.error(f'no active workflows to be started, exiting')
            quit(1)

    def gather_wallets(self):
        """
        go through config, and find all enabled workflows to
        gather the decryption keys and return the decryption keys
        to launch the workflows
        """
        workflows = self.config.workflows
        wallet_files = []
        for e in workflows:
            workflow = workflows[e]
            if not workflow.disabled and len(workflow.wallet_file) > 0 and workflow.wallet_file not in wallet_files:
                wallet_files.append(workflow.wallet_file)

        wallet_keys = {}

        for e in wallet_files:
            dw = False
            while not dw:                    
                pw = getpass(prompt = f'enter decryption key for {e}: ')
                dw = load_encrypted_wallets(e, pw)
                if not dw:
                    print(f'incorrect decryption key for {e}, try again!')
            if dw:
                wallet_keys[e] = pw

        del dw
        return wallet_keys


