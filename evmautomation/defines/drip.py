import json

DRIP_TOKEN_CONTRACT_ADDRESS = "0x20f663CEa80FaCE82ACDFA3aAE6862d246cE0333"
DRIP_TOKEN_ABI = [
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"mintingFinished",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"name",
      "outputs":[
         {
            "name":"",
            "type":"string"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_spender",
            "type":"address"
         },
         {
            "name":"_value",
            "type":"uint256"
         }
      ],
      "name":"approve",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"MAX_INT",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"player",
            "type":"address"
         }
      ],
      "name":"statsOf",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         },
         {
            "name":"",
            "type":"uint256"
         },
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"totalSupply",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_from",
            "type":"address"
         },
         {
            "name":"_to",
            "type":"address"
         },
         {
            "name":"_value",
            "type":"uint256"
         }
      ],
      "name":"transferFrom",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"addrs",
            "type":"address[]"
         }
      ],
      "name":"removeAddressesFromWhitelist",
      "outputs":[
         {
            "name":"success",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"removeAddressFromWhitelist",
      "outputs":[
         {
            "name":"success",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"targetSupply",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"decimals",
      "outputs":[
         {
            "name":"",
            "type":"uint8"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"remainingMintableSupply",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"cap",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"player",
            "type":"address"
         }
      ],
      "name":"mintedBy",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_to",
            "type":"address"
         },
         {
            "name":"_amount",
            "type":"uint256"
         }
      ],
      "name":"mint",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"account",
            "type":"address"
         },
         {
            "name":"taxRate",
            "type":"uint8"
         }
      ],
      "name":"setAccountCustomTax",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"vaultAddress",
      "outputs":[
         {
            "name":"",
            "type":"address"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"totalTxs",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_spender",
            "type":"address"
         },
         {
            "name":"_subtractedValue",
            "type":"uint256"
         }
      ],
      "name":"decreaseApproval",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"_owner",
            "type":"address"
         }
      ],
      "name":"balanceOf",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"account",
            "type":"address"
         }
      ],
      "name":"removeAccountCustomTax",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"_from",
            "type":"address"
         },
         {
            "name":"_value",
            "type":"uint256"
         }
      ],
      "name":"calculateTransferTaxes",
      "outputs":[
         {
            "name":"adjustedValue",
            "type":"uint256"
         },
         {
            "name":"taxAmount",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"addAddressToWhitelist",
      "outputs":[
         {
            "name":"success",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         
      ],
      "name":"finishMinting",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_newVaultAddress",
            "type":"address"
         }
      ],
      "name":"setVaultAddress",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"owner",
      "outputs":[
         {
            "name":"",
            "type":"address"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"symbol",
      "outputs":[
         {
            "name":"",
            "type":"string"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"",
            "type":"address"
         }
      ],
      "name":"whitelist",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_to",
            "type":"address"
         },
         {
            "name":"_value",
            "type":"uint256"
         }
      ],
      "name":"transfer",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"mintedSupply",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"account",
            "type":"address"
         }
      ],
      "name":"isExcluded",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"_spender",
            "type":"address"
         },
         {
            "name":"_addedValue",
            "type":"uint256"
         }
      ],
      "name":"increaseApproval",
      "outputs":[
         {
            "name":"",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         
      ],
      "name":"players",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":True,
      "inputs":[
         {
            "name":"_owner",
            "type":"address"
         },
         {
            "name":"_spender",
            "type":"address"
         }
      ],
      "name":"allowance",
      "outputs":[
         {
            "name":"",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"view",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"addrs",
            "type":"address[]"
         }
      ],
      "name":"addAddressesToWhitelist",
      "outputs":[
         {
            "name":"success",
            "type":"bool"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"account",
            "type":"address"
         }
      ],
      "name":"excludeAccount",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"newOwner",
            "type":"address"
         }
      ],
      "name":"transferOwnership",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "constant":False,
      "inputs":[
         {
            "name":"account",
            "type":"address"
         }
      ],
      "name":"includeAccount",
      "outputs":[
         
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "name":"_initialMint",
            "type":"uint256"
         }
      ],
      "payable":False,
      "stateMutability":"nonpayable",
      "type":"constructor"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "name":"from",
            "type":"address"
         },
         {
            "indexed":False,
            "name":"vault",
            "type":"address"
         },
         {
            "indexed":False,
            "name":"amount",
            "type":"uint256"
         }
      ],
      "name":"TaxPayed",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "name":"to",
            "type":"address"
         },
         {
            "indexed":False,
            "name":"amount",
            "type":"uint256"
         }
      ],
      "name":"Mint",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         
      ],
      "name":"MintFinished",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"WhitelistedAddressAdded",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"WhitelistedAddressRemoved",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "name":"previousOwner",
            "type":"address"
         },
         {
            "indexed":True,
            "name":"newOwner",
            "type":"address"
         }
      ],
      "name":"OwnershipTransferred",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "name":"owner",
            "type":"address"
         },
         {
            "indexed":True,
            "name":"spender",
            "type":"address"
         },
         {
            "indexed":False,
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"Approval",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "name":"from",
            "type":"address"
         },
         {
            "indexed":True,
            "name":"to",
            "type":"address"
         },
         {
            "indexed":False,
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"Transfer",
      "type":"event"
   }
]

DRIP_FAUCET_CONTRACT_ADDRESS = "0xFFE811714ab35360b67eE195acE7C10D93f89D8C"
DRIP_FAUCET_ABI = json.loads('''
  [
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "_src",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "_dest",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "_deposits",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "_payouts",
          "type": "uint256"
        }
      ],
      "name": "BalanceTransfer",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "beneficiary",
          "type": "address"
        }
      ],
      "name": "BeneficiaryUpdate",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        }
      ],
      "name": "Checkin",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "DirectPayout",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        }
      ],
      "name": "HeartBeat",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "interval",
          "type": "uint256"
        }
      ],
      "name": "HeartBeatIntervalUpdate",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "referrals",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "total_deposits",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "total_payouts",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "total_structure",
          "type": "uint256"
        }
      ],
      "name": "Leaderboard",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "LimitReached",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        }
      ],
      "name": "ManagerUpdate",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "MatchPayout",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "timestamp",
          "type": "uint256"
        }
      ],
      "name": "NewAirdrop",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "NewDeposit",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "upline",
          "type": "address"
        }
      ],
      "name": "Upline",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "addr",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Withdraw",
      "type": "event"
    },
    {
      "stateMutability": "payable",
      "type": "fallback"
    },
    {
      "inputs": [],
      "name": "CompoundTax",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "ExitTax",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "MAX_UINT",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "airdrop",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "airdrops",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "airdrops",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "airdrops_received",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "last_airdrop",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "balanceLevel",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "checkin",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "claim",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "claimsAvailable",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "contractInfo",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "_total_users",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_total_deposited",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_total_withdraw",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_total_bnb",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_total_txs",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_total_airdrops",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "creditsAndDebits",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "_credits",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_debits",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "custody",
      "outputs": [
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "beneficiary",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "last_heartbeat",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "last_checkin",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "heartbeat_interval",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_upline",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "deposit",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "deposit_bracket_size",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "dripVaultAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "getCustody",
      "outputs": [
        {
          "internalType": "address",
          "name": "_beneficiary",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_heartbeat_interval",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "_manager",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "initialize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        },
        {
          "internalType": "uint8",
          "name": "_level",
          "type": "uint8"
        }
      ],
      "name": "isBalanceCovered",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "isNetPositive",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "lastActivity",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "_heartbeat",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_lapsed_heartbeat",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_checkin",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_lapsed_checkin",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "maxPayoutOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "max_payout_cap",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "payoutOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "payout",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "max_payout",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "net_payout",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "sustainability_fee",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "ref_balances",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "roll",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "_pendingDiv",
          "type": "uint256"
        }
      ],
      "name": "sustainabilityFeeV2",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_airdrops",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_bnb",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_deposited",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_txs",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_users",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "total_withdraw",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newCompoundTax",
          "type": "uint256"
        }
      ],
      "name": "updateCompoundTax",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newBracketSize",
          "type": "uint256"
        }
      ],
      "name": "updateDepositBracketSize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newExitTax",
          "type": "uint256"
        }
      ],
      "name": "updateExitTax",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256[]",
          "name": "_newRefBalances",
          "type": "uint256[]"
        }
      ],
      "name": "updateHoldRequirements",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newInitialDeposit",
          "type": "uint256"
        }
      ],
      "name": "updateInitialDeposit",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newPayoutCap",
          "type": "uint256"
        }
      ],
      "name": "updateMaxPayoutCap",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newPayoutRate",
          "type": "uint256"
        }
      ],
      "name": "updatePayoutRate",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newRefBonus",
          "type": "uint256"
        }
      ],
      "name": "updateRefBonus",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_newRefDepth",
          "type": "uint256"
        }
      ],
      "name": "updateRefDepth",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "userInfo",
      "outputs": [
        {
          "internalType": "address",
          "name": "upline",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "deposit_time",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "deposits",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "payouts",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "direct_bonus",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "match_bonus",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "last_airdrop",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_addr",
          "type": "address"
        }
      ],
      "name": "userInfoTotals",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "referrals",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "total_deposits",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "total_payouts",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "total_structure",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "airdrops_total",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "airdrops_received",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "users",
      "outputs": [
        {
          "internalType": "address",
          "name": "upline",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "referrals",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "total_structure",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "direct_bonus",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "match_bonus",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "deposits",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "deposit_time",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "payouts",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "rolls",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "ref_claim_pos",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "accumulatedDiv",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]
''')
    
DRIP_FOUNTAIN_CONTRACT_ADDRESS = "0x4Fe59AdcF621489cED2D674978132a54d432653A"
DRIP_FOUNTAIN_ABI = [
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"token_addr",
            "type":"address"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"constructor"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"owner",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"address",
            "name":"spender",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"Approval",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"previousOwner",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"address",
            "name":"newOwner",
            "type":"address"
         }
      ],
      "name":"OwnershipTransferred",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"from",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"address",
            "name":"to",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"Transfer",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"address",
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"WhitelistedAddressAdded",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"address",
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"WhitelistedAddressRemoved",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"provider",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"bnb_amount",
            "type":"uint256"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"token_amount",
            "type":"uint256"
         }
      ],
      "name":"onAddLiquidity",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"buyer",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"token_amount",
            "type":"uint256"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"bnb_amount",
            "type":"uint256"
         }
      ],
      "name":"onBnbPurchase",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"balance",
            "type":"uint256"
         }
      ],
      "name":"onContractBalance",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"provider",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         }
      ],
      "name":"onLiquidity",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"price",
            "type":"uint256"
         }
      ],
      "name":"onPrice",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"provider",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"bnb_amount",
            "type":"uint256"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"token_amount",
            "type":"uint256"
         }
      ],
      "name":"onRemoveLiquidity",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"liquidity",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"price",
            "type":"uint256"
         }
      ],
      "name":"onSummary",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"buyer",
            "type":"address"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"bnb_amount",
            "type":"uint256"
         },
         {
            "indexed":True,
            "internalType":"uint256",
            "name":"token_amount",
            "type":"uint256"
         }
      ],
      "name":"onTokenPurchase",
      "type":"event"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"addAddressToWhitelist",
      "outputs":[
         {
            "internalType":"bool",
            "name":"success",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address[]",
            "name":"addrs",
            "type":"address[]"
         }
      ],
      "name":"addAddressesToWhitelist",
      "outputs":[
         {
            "internalType":"bool",
            "name":"success",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"min_liquidity",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"max_tokens",
            "type":"uint256"
         }
      ],
      "name":"addLiquidity",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"payable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"owner",
            "type":"address"
         },
         {
            "internalType":"address",
            "name":"spender",
            "type":"address"
         }
      ],
      "name":"allowance",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"spender",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"approve",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"owner",
            "type":"address"
         }
      ],
      "name":"balanceOf",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"bnbBalance",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"min_tokens",
            "type":"uint256"
         }
      ],
      "name":"bnbToTokenSwapInput",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"payable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"tokens_bought",
            "type":"uint256"
         }
      ],
      "name":"bnbToTokenSwapOutput",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"payable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"decimals",
      "outputs":[
         {
            "internalType":"uint8",
            "name":"",
            "type":"uint8"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"spender",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"subtractedValue",
            "type":"uint256"
         }
      ],
      "name":"decreaseAllowance",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"bnb_sold",
            "type":"uint256"
         }
      ],
      "name":"getBnbToLiquidityInputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"bnb_sold",
            "type":"uint256"
         }
      ],
      "name":"getBnbToTokenInputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"tokens_bought",
            "type":"uint256"
         }
      ],
      "name":"getBnbToTokenOutputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"input_amount",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"input_reserve",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"output_reserve",
            "type":"uint256"
         }
      ],
      "name":"getInputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         }
      ],
      "name":"getLiquidityToReserveInputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"output_amount",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"input_reserve",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"output_reserve",
            "type":"uint256"
         }
      ],
      "name":"getOutputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"tokens_sold",
            "type":"uint256"
         }
      ],
      "name":"getTokenToBnbInputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"bnb_bought",
            "type":"uint256"
         }
      ],
      "name":"getTokenToBnbOutputPrice",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"spender",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"addedValue",
            "type":"uint256"
         }
      ],
      "name":"increaseAllowance",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"isPaused",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"name",
      "outputs":[
         {
            "internalType":"string",
            "name":"",
            "type":"string"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"owner",
      "outputs":[
         {
            "internalType":"address",
            "name":"",
            "type":"address"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"pause",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"providers",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"addr",
            "type":"address"
         }
      ],
      "name":"removeAddressFromWhitelist",
      "outputs":[
         {
            "internalType":"bool",
            "name":"success",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address[]",
            "name":"addrs",
            "type":"address[]"
         }
      ],
      "name":"removeAddressesFromWhitelist",
      "outputs":[
         {
            "internalType":"bool",
            "name":"success",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"min_bnb",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"min_tokens",
            "type":"uint256"
         }
      ],
      "name":"removeLiquidity",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"symbol",
      "outputs":[
         {
            "internalType":"string",
            "name":"",
            "type":"string"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"tokenAddress",
      "outputs":[
         {
            "internalType":"address",
            "name":"",
            "type":"address"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"tokenBalance",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"tokens_sold",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"min_bnb",
            "type":"uint256"
         }
      ],
      "name":"tokenToBnbSwapInput",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"bnb_bought",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"max_tokens",
            "type":"uint256"
         }
      ],
      "name":"tokenToBnbSwapOutput",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"totalSupply",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"totalTxs",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"to",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"transfer",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"from",
            "type":"address"
         },
         {
            "internalType":"address",
            "name":"to",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"value",
            "type":"uint256"
         }
      ],
      "name":"transferFrom",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"newOwner",
            "type":"address"
         }
      ],
      "name":"transferOwnership",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"owner",
            "type":"address"
         }
      ],
      "name":"txs",
      "outputs":[
         {
            "internalType":"uint256",
            "name":"",
            "type":"uint256"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"unpause",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"",
            "type":"address"
         }
      ],
      "name":"whitelist",
      "outputs":[
         {
            "internalType":"bool",
            "name":"",
            "type":"bool"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "stateMutability":"payable",
      "type":"receive"
   }
]

DRIP_GARDEN_CONTRACT_ADDRESS = "0x685BFDd3C2937744c13d7De0821c83191E3027FF"
DRIP_GARDEN_ABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "ref",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amountBNB",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amountEggs",
        "type": "uint256"
      }
    ],
    "name": "SeedsBought",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "ref",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "seedsUsed",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "marketSeeds",
        "type": "uint256"
      }
    ],
    "name": "SeedsPlanted",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "seedsSold",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "seedValue",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "marketSeeds",
        "type": "uint256"
      }
    ],
    "name": "SeedsSold",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "BusdAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "DripAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "DripBusdLp",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "DripVaultAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "MarketingAndDevelopmentAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "PancakeSwapRouter",
    "outputs": [
      {
        "internalType": "contract IUniswapV2Router01",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "PancakeSwapRouterAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "SEEDS_TO_GROW_1PLANT",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "ref",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "buySeeds",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "seeds",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedSell",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "contractBalance",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuy",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuySimple",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuySimpleBalance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuySimpleTime",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuySimpleTotal",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "bnb",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "contractBalance",
        "type": "uint256"
      }
    ],
    "name": "calculateSeedsBuyTotal",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "rt",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "rs",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "bs",
        "type": "uint256"
      }
    ],
    "name": "calculateTrade",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "claimedSeeds",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "currentBalanceMultiplier",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "currentTimeMultiplier",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "devFee",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getBalance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getMyPlants",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getMySeeds",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "adr",
        "type": "address"
      }
    ],
    "name": "getSeedsSinceLastPlant",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_user",
        "type": "address"
      }
    ],
    "name": "getUserSeeds",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "hatcheryPlants",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "initialized",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "lastPlant",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "marketSeeds",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "ref",
        "type": "address"
      }
    ],
    "name": "plantSeeds",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "referrals",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "renounceOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "seedMarket",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "sellSeeds",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_top",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "multiplier",
        "type": "uint256"
      }
    ],
    "name": "setBalanceMultiplier",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_seed",
        "type": "uint256"
      }
    ],
    "name": "setSeedAmount",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "startTime",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
