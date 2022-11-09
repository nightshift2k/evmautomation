from audioop import add
import arrow
import logging
import random
from time import sleep
from typing import List
from telebot import TeleBot
from threading import Thread
from evmautomation.defines.generic import LOOP_SLEEP_TIME
from evmautomation.tools.encryption import load_encrypted_wallets
from evmautomation.tools.config import Config
from evmautomation.tools.rpc import get_fastest_rpc_url, get_healthy_rpc_urls
from sqlitedict import SqliteDict

from typing import List

LOG = logging.getLogger('evmautomation')

class BaseWorkflow(Thread):

    config = None
    telebot = None
    decryption_key = None
    pstore: SqliteDict # private store per workflow
    cstore: SqliteDict # chain store

    def __init__(self, config=None, decryption_key: str = None) -> None:
        """
        Initializes the module with given config
        """
        Thread.__init__(self)
        self.config = Config(config)
        self.decryption_key = decryption_key
        LOG.debug(f'initializing {self.__class__.__name__}')

        if self.config.telegram.bot_token and self.config.telegram.chat_id and self.config.telegram.disabled != True:
            LOG.debug(f'setting up telegram bot to talk to {self.config.telegram.chat_id}')
            self.telebot = TeleBot(self.config.telegram.bot_token, parse_mode="Markdown")

        self.init_persistence() # init table inside peristence database

    def load_wallets(self, wallet_file):
        self.wallets = load_encrypted_wallets(wallet_file, self.decryption_key)
        if isinstance(self.wallets, List) and len(self.wallets) > 0:
            LOG.debug(f'loaded {len(self.wallets)} wallet(s) from {wallet_file}')
        else:
            LOG.warn(f'no wallets loaded from {wallet_file}, check file and/or encryption key?!')

    def tg_send_msg(self, message: str, address: str = None) -> None:
        if isinstance(self.telebot, TeleBot) and self.config.telegram.disabled != True:

            if isinstance(address, str):
                message = message + \
                f'\n\n' \
                f'==============\n\n' \
                f'*Wallet Address:*\n' \
                f'`{address}`'
            self.telebot.send_message(self.config.telegram.chat_id, message)


    def get_fastest_rpc_url(self, urls: List) -> str:
        if len(urls) > 1:
            fastest_url = get_fastest_rpc_url(urls)
            LOG.debug(f'fastest endpoint is {fastest_url}')
        else:
            fastest_url = urls[0]
        return fastest_url

    def get_healthy_rpc_urls(self, urls: List, exclude_url: str = "") -> List:
        healthy_urls = get_healthy_rpc_urls(urls)
        if len(exclude_url) > 0:
            if exclude_url in healthy_urls:
                healthy_urls.remove(exclude_url)
        return healthy_urls


    def init_persistence(self):
        ptable = self.config.chain+"-"+self.config.name
        self.pstore = SqliteDict(self.config.db_file, tablename=ptable, autocommit=True)
        LOG.debug(f'{self.config.db_file} persistence database for workflow = {ptable}')
        self.cstore = SqliteDict(self.config.db_file, tablename=self.config.chain, autocommit=True)
        LOG.debug(f'{self.config.db_file} persistence database for chain = {self.config.chain}')

    def sleep_between_loops(self):
        sleep(LOOP_SLEEP_TIME)


    def get_next_run(self, address: str) -> int:
        if isinstance(self.pstore, SqliteDict):
            k = address + '_' + 'next_run'
            ts = int(self.pstore[k] if k in list(self.pstore.keys()) else 0)
            return ts
        else:
            return 0
    
    def set_next_run(self, address: str, next_run_secs: int) -> bool:
        if isinstance(self.pstore, SqliteDict):
            k = address + '_' + 'next_run'
            ts = arrow.utcnow().int_timestamp + next_run_secs
            self.pstore[k] = ts
            LOG.debug(f'wallet {address} - sleeping {next_run_secs} seconds ...')
            return True
        else:
            return False

    def need_to_run(self, address: str) -> bool:
        if arrow.utcnow().int_timestamp >= self.get_next_run(address):
            return True
        else:
            return False

    def random_wait(self, minw, maxw):
        sleep(random.randint(minw, maxw))