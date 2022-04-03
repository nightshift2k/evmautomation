import logging
from time import process_time
from typing import Dict, List
import requests
import operator
from tenacity import *

LOG = logging.getLogger('evmautomation')

@retry(stop=stop_after_attempt(5), wait=wait_fixed(1))
def get_rpc_latency(url: str) -> Dict:
    request_data = {"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}
    result = False
    t_start = process_time()
    response = requests.post(url, json=request_data)
    t_stop = process_time()
    pdiff = int(( 1000* (t_stop - t_start ) ))
    obj = response.json()
    if 'result' in obj:
        result = {
            'endpoint': url,
            'latency': pdiff,
            'blocknumber': int(obj['result'], 16)
        }

    return result

def get_fastest_rpc_url(urls: List) -> str:
    results = []
    for url in urls:
        try:
            result = False
            result = get_rpc_latency(url)
        except Exception as e:
            LOG.warning(f'connection error while testing {url}, endpoint will be skipped')
            pass
        if isinstance(result, Dict):
            results.append(result)
    
    results.sort(key=operator.itemgetter('latency'))
    return results[0]['endpoint']
