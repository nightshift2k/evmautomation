"""
PancakeSwap Router Contract Subclass
"""

from decimal import Decimal
from evmautomation.contracts import BscContract, BEP20TokenContract
from evmautomation.defines.pcs import PCS_ROUTER_ADDRESS, PCS_ROUTER_ABI, PCS_BNB_BUSD_PATH

class PancakeSwapRouterContract(BscContract):
    
    def __init__(self, rpc_url: str, wallet_address: str) -> None:
        """
        Initializes the super class but provides
        contract address and abi for simplicity reasons.
        """        
        super().__init__(rpc_url, PCS_ROUTER_ADDRESS, PCS_ROUTER_ABI, wallet_address)


    def get_amounts_out(self, amount, path):
        if isinstance(path, list) and len(path) >= 2:
            in_token = path[0]
            out_token = path[-1]
            in_contract = BEP20TokenContract(self._rpc_url, self._wallet, in_token)
            out_contract = BEP20TokenContract(self._rpc_url, self._wallet, out_token)
            in_amount = int(amount * (10 ** in_contract.get_decimals()))
            _, ret_out = self._contract.functions.getAmountsOut(in_amount, path).call()
            out_amount = Decimal(ret_out / (10 ** out_contract.get_decimals()))
            return out_amount
        else:
            return False


    def get_swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens_transaction(
            self, 
            amount_in, 
            amount_out_min, 
            path, 
            to, 
            deadline: int, 
            gas=600000
        ):
        if isinstance(path, list) and len(path) >= 2:
            in_token = path[0]
            out_token = path[-1]
            in_contract = BEP20TokenContract(self._rpc_url, self._wallet, in_token)
            out_contract = BEP20TokenContract(self._rpc_url, self._wallet, out_token)
            in_amount = int(amount_in * (10 ** in_contract.get_decimals()))
            out_amount = int(amount_out_min * (10 ** out_contract.get_decimals()))

            tx = self._contract.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(
                in_amount,
                out_amount,
                path,
                to,
                deadline
            ).build_transaction(self.get_transaction_options(gas))
            return tx
        else:
            return False

    """
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);    
    """
    def get_swap_exact_tokens_for_tokens_transaction(
            self, 
            amount_in, 
            amount_out_min, 
            path, 
            to, 
            deadline: int, 
            gas=600000
        ):
        if isinstance(path, list) and len(path) >= 2:
            in_token = path[0]
            out_token = path[-1]
            in_contract = BEP20TokenContract(self._rpc_url, self._wallet, in_token)
            out_contract = BEP20TokenContract(self._rpc_url, self._wallet, out_token)
            in_amount = int(amount_in * (10 ** in_contract.get_decimals()))
            out_amount = int(amount_out_min * (10 ** out_contract.get_decimals()))

            tx = self._contract.functions.swapExactTokensForTokens(
                in_amount,
                out_amount,
                path,
                to,
                deadline
            ).build_transaction(self.get_transaction_options(gas))
            return tx
        else:
            return False


    def get_swap_exact_eth_for_tokens_transaction(
            self, 
            amount_in, 
            amount_out_min, 
            path, 
            to, 
            deadline: int, 
            gas=600000
        ):
        if isinstance(path, list) and len(path) >= 2:
            in_token = path[0]
            out_token = path[-1]
            in_contract = BEP20TokenContract(self._rpc_url, self._wallet, in_token)
            out_contract = BEP20TokenContract(self._rpc_url, self._wallet, out_token)
            in_amount = int(amount_in * (10 ** in_contract.get_decimals()))
            out_amount = int(amount_out_min * (10 ** out_contract.get_decimals()))

            tx = self._contract.functions.swapExactETHForTokens(
                out_amount,
                path,
                to,
                deadline
            ).build_transaction(self.get_transaction_options(gas, value=in_amount)) # amount in as tx options
            return tx
        else:
            return False
    
    def get_bnb_price(self):
        return self.get_amounts_out(1, PCS_BNB_BUSD_PATH)