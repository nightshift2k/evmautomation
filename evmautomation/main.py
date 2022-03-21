#!/usr/bin/env python3
import argparse
import logging
from os import path
import sys
from cryptography.fernet import Fernet
from evmautomation.tools.encryption import encrypt_wallet_csv
from evmautomation.evmautomation import EVMAutomation

# check min. python version
if sys.version_info < (3, 8):
    sys.exit("EVMAutomation requires Python version >= 3.8")

LOG = logging.getLogger('evmautomation')



def encrypt_file(infile, outfile):
    if path.isfile(infile):
        key = Fernet.generate_key()
        try:
            print(f'encrypting {infile} to {outfile}')
            encrypt_wallet_csv(infile, outfile, key, False)
            print(f'encryption key for {outfile} is: {key.decode()}')
            print(f'please store this key safely!')
        except Exception as e:
            print(f'error while encrypting: {e}')
    else:
        print(f'{infile} not found')

def main():
    return_code = 0
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-c", 
            "--config",
            nargs=1,
            type=str,
            default="config.yaml",
            help='path to the config file'
        )

        parser.add_argument(
            '-r',
            '--run',
            action='store_true',
            default=False,
            help='Run evm automation workflows configured in config.yaml or custom config file (specify with -c)'
        )

        parser.add_argument(
            '-e',
            '--encrypt',
            nargs=2,
            metavar=('INFILE', 'OUTFILE'),
            help='encrypts infile.csv to outfile.json and displays the encryption key'
        )

        if len(sys.argv)==1:
            parser.print_help(sys.stderr)
            sys.exit(1)        
        
        args = parser.parse_args()

        # if encrypt
        if (args.encrypt):
            encrypt_file(args.encrypt[0], args.encrypt[1])
            sys.exit(0)

        elif(args.run):
            ea = EVMAutomation(config=args.config)
            ea.run()

    except SystemExit as e:
        return_code = e
    except KeyboardInterrupt:
        LOG.info('SIGINT received, aborting ...')
    except Exception:
        LOG.exception('Fatal exception!')
        return_code = 1
    finally:
        sys.exit(return_code)

if __name__ == '__main__':
    main()
