import logging
from typing import List
from telebot import TeleBot
from threading import Thread
from evmautomation.tools.encryption import load_encrypted_wallets
from evmautomation.tools.config import Config

LOG = logging.getLogger('evmautomation')

class BaseWorkflow(Thread):

    config = None
    telebot = None
    decryption_key = None

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

    def load_wallets(self, wallet_file):
        self.wallets = load_encrypted_wallets(wallet_file, self.decryption_key)
        if isinstance(self.wallets, List) and len(self.wallets) > 0:
            LOG.debug(f'loaded {len(self.wallets)} wallet(s) from {wallet_file}')
        else:
            LOG.warn(f'no wallets loaded from {wallet_file}, check file and/or encryption key?!')

    def tg_send_msg(self, message: str, wallet: str = None) -> None:
        if isinstance(self.telebot, TeleBot) and self.config.telegram.disabled != True:

            if len(wallet) > 0:
                message = message + \
                f'\n\n' \
                f'==============\n\n' \
                f'*Wallet Address:*\n' \
                f'`{wallet}`'
            self.telebot.send_message(self.config.telegram.chat_id, message)
