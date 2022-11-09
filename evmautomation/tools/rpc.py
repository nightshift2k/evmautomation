import logging
from time import process_time
from typing import Dict, List
import requests
import operator
from tenacity import *

LOG = logging.getLogger('evmautomation')

@retry(stop=stop_after_attempt(5), wait=wait_fixed(1))
def get_rpc_latency(url: str) -> Dict:
    t_start = process_time()
    blocknumber = check_rpc_health(url)
    t_stop = process_time()
    pdiff = int(( 1000* (t_stop - t_start ) ))

    if blocknumber:
        return {
            'endpoint': url,
            'latency': pdiff,
            'blocknumber': blocknumber
        }
    else:
        return False

def get_healthy_rpc_urls(urls: List) -> List:
    healthy_urls = []
    for url in urls:
        try:
            result = False
            result = check_rpc_health(url)
        except Exception as e:
            LOG.warning(f'connection error while testing {url}, endpoint will be skipped')
            pass
        if result > 0:
            healthy_urls.append(url)
        else:
            LOG.warning(f'{url} has not returned a valid blocknumber and will be skipped')
    return healthy_urls


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

@retry(stop=stop_after_attempt(5), wait=wait_fixed(1))
def check_rpc_health(url: str):
    request_data = {"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}
    response = requests.post(url, json=request_data)
    obj = response.json()

    bn = 0
    if 'result' in obj:
        bn = int(obj['result'], 16)

    return bn