import csv, json, logging, os
from cryptography.fernet import Fernet
from typing import List

LOG = logging.getLogger('evmautomation')


def encrypt_wallet_csv(infile, outfile, key, del_infile=True) -> bool:
    with open(infile, "rb") as infile_obj:
        # read all file data
        in_data = infile_obj.read()

    f = Fernet(key)

    wallets = [row for row in csv.reader([line.decode() for line in in_data.splitlines()], delimiter=';')]

    if len(wallets) < 1:
        return False

    encodedWallets = []
    for wallet in wallets:
        encodedWallets.append(
            [
                f.encrypt(wallet[0].encode()).decode(),
                f.encrypt(wallet[1].encode()).decode()
            ]
        )

    with open(outfile, "w", encoding="utf-8") as outfile_obj:
        json.dump(encodedWallets, outfile_obj, ensure_ascii=False, indent=4)

    if del_infile:
        os.remove(infile)
        
    return True

def load_encrypted_wallets(infile, key) -> List:
    try:
        with open(infile, "rb") as infile_obj:
            # read all file data
            encodedWallets = json.load(infile_obj)
    except FileNotFoundError:
        LOG.error(f'{infile} not found')
        return False
    try:
        f = Fernet(key)
    except Exception as e:
        LOG.error(f'fernet key error: {e}')
        return False

    if len(encodedWallets) < 1:
        LOG.error('no wallet entries found in json or wrong structure!')
        return False

    decodedWallets = []
    for wallet in encodedWallets:
        decodedWallets.append(
            [
                f.decrypt(wallet[0].encode()).decode(),
                f.decrypt(wallet[1].encode()).decode()
            ]
        )
    
    return decodedWallets