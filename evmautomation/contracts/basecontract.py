"""
Basic Wrapper for Web3 functions
"""

from web3 import Web3
from web3.contract import Contract
from typing import Any, List

class BaseContract:
    """
    Base Class for Web3 contract interaction.
    """

    _web3: Web3 
    _contract: Contract
    _wallet: Any

    def __init__(self, rpc_url: str, contract_address: str, abi: List, wallet_address: str) -> None:
        """
        Initializes the module with given config
        """

        self._web3 = Web3(Web3.HTTPProvider(rpc_url))
        self._contract = self._web3.eth.contract(address=contract_address, abi=abi)
        self._wallet = wallet_address

    def get_transaction_options(self, gas=500000):
        """
        returns a dict with transaction options
        """

        return {
            "nonce": self._web3.eth.getTransactionCount(self._wallet),
            "from": self._wallet,
            "gas": gas,
            "gasPrice": self._web3.eth.gas_price
        }

    def send_transaction(self, transaction, private_key):
        """
        Signs the provided transaction with a privat key
        and executes it. Waits upon result.
        """

        txns = self._web3.eth.account.sign_transaction(transaction, private_key)
        txnh = self._web3.eth.send_raw_transaction(txns.rawTransaction)
        txnr = self._web3.eth.wait_for_transaction_receipt(txnh)
        return txnr


    def estimate_gas_fees(self, transaction):
        """
        Estimates gas fees for a submitted transaction.
        """
        try:
            gas = self._web3.eth.estimate_gas(transaction)
        except Exception as e:
             gas = False
        return gas

#

    def estimate_transaction_fees(self, transaction):
        """
        Estimates transaction fees for a submitted transaction.
        Gas is multiplied by price to reflect the fees
        in native token price.
        """

        gas = self.estimate_gas_fees(transaction)            
        if gas > 0:
            gasprice = self.get_gas_price()
            return gas * gasprice
        else:
            return False

    def get_balance(self):
        """
        basic balance function to get the balance for
        the native token.
        """

        balance = self._web3.fromWei(self._web3.eth.getBalance(self._wallet), "ether")
        return balance

    def get_gas_price(self):
        return self._web3.fromWei(self._web3.eth.gas_price, "ether")