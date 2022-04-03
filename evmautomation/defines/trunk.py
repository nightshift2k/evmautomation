# FlowEngine
TRUNK_STAMPEDE_CONTRACT_ADDRESS = "0x6839e295a8f13864A2830fA0dCC0F52e71a82DbF"
TRUNK_STAMPEDE_ABI = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "BuyBack",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "total_deposits",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "total_payouts",
				"type": "uint256"
			}
		],
		"name": "Leaderboard",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "LimitReached",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "NewDeposit",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "NewSponsorship",
		"type": "event"
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
				"name": "addr",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "Withdraw",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "DepositTax",
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
		"inputs": [],
		"name": "backedAddress",
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
		"name": "backedToken",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "backedTreasury",
		"outputs": [
			{
				"internalType": "contract ITreasury",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "backedTreasuryAddress",
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
		"name": "collateralAddress",
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
		"name": "collateralRouter",
		"outputs": [
			{
				"internalType": "contract IUniswapV2Router02",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "collateralToken",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
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
				"name": "_total_txs",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_total_sponsorships",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "coreAddress",
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
		"name": "coreToken",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "coreTreasury",
		"outputs": [
			{
				"internalType": "contract ITreasury",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "coreTreasuryAddress",
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
		"name": "flowData",
		"outputs": [
			{
				"internalType": "contract FlowData",
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
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "preserveBacked",
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
				"internalType": "bool",
				"name": "_preserve",
				"type": "bool"
			}
		],
		"name": "preserveBackedSupply",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "referralData",
		"outputs": [
			{
				"internalType": "contract ReferralData",
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
		"inputs": [],
		"name": "reserve",
		"outputs": [
			{
				"internalType": "contract IElephantReserve",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
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
		"inputs": [],
		"name": "rollBalance",
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
		"name": "router",
		"outputs": [
			{
				"internalType": "contract IUniswapV2Router02",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "routerAddress",
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
		"name": "slippageRate",
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
				"name": "_addr",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "sponsor",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "sponsorData",
		"outputs": [
			{
				"internalType": "contract SponsorData",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "sweep",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "sweepThreshold",
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
				"internalType": "address",
				"name": "_router",
				"type": "address"
			}
		],
		"name": "updateCollateralRouter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "flowDataAddress",
				"type": "address"
			}
		],
		"name": "updateFlowData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "referralDataAddress",
				"type": "address"
			}
		],
		"name": "updateReferralData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "reserveAddress",
				"type": "address"
			}
		],
		"name": "updateReserve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_rate",
				"type": "uint256"
			}
		],
		"name": "updateSlippageRate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sponsorDataAddress",
				"type": "address"
			}
		],
		"name": "updateSponsorData",
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
				"name": "pending_sponsorship",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "total_sponsorship",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "wethToken",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# BankrollNetworkStack
TRUNK_NATIVE_STAKING_CONTRACT_ADDRESS = "0xec10059BA900883ed6154883E9f3A1C24fcE1eb7" 
TRUNK_NATIVE_STAKING_ABI = [
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"_tokenAddress",
            "type":"address"
         },
         {
            "internalType":"address",
            "name":"_tokenRouter",
            "type":"address"
         },
         {
            "internalType":"uint8",
            "name":"_fee",
            "type":"uint8"
         },
         {
            "internalType":"uint8",
            "name":"_payout",
            "type":"uint8"
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
            "indexed":False,
            "internalType":"uint256",
            "name":"balance",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onBalance",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onBuyBack",
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
            "indexed":False,
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onDonation",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"customerAddress",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"invested",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"tokens",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"soldTokens",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onLeaderBoard",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"customerAddress",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"ethReinvested",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"tokensMinted",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onReinvestment",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"customerAddress",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"incomingeth",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"tokensMinted",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onTokenPurchase",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"customerAddress",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"tokensBurned",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"ethEarned",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onTokenSell",
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
            "name":"tokens",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onTransfer",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":True,
            "internalType":"address",
            "name":"customerAddress",
            "type":"address"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"ethWithdrawn",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onWithdraw",
      "type":"event"
   },
   {
      "inputs":[
         
      ],
      "name":"balanceInterval",
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
            "name":"_customerAddress",
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
         {
            "internalType":"uint256",
            "name":"buy_amount",
            "type":"uint256"
         }
      ],
      "name":"buy",
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
            "internalType":"address",
            "name":"_customerAddress",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"buy_amount",
            "type":"uint256"
         }
      ],
      "name":"buyFor",
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
      "name":"buyPrice",
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
      "name":"buybackEnabled",
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
         {
            "internalType":"uint256",
            "name":"_ethToSpend",
            "type":"uint256"
         }
      ],
      "name":"calculateTokensReceived",
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
            "name":"_tokensToSell",
            "type":"uint256"
         }
      ],
      "name":"calculateethReceived",
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
            "name":"_customerAddress",
            "type":"address"
         }
      ],
      "name":"dailyEstimate",
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
      "name":"distributionInterval",
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
      "name":"dividendBalance_",
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
            "name":"_customerAddress",
            "type":"address"
         }
      ],
      "name":"dividendsOf",
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
      "name":"donatePool",
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
      "name":"elephantAddress",
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
      "name":"elephantReserve_",
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
            "internalType":"bool",
            "name":"enable",
            "type":"bool"
         }
      ],
      "name":"enableBuyback",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"firstBlock",
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
      "name":"firstTimestamp",
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
      "name":"graveyardAddress",
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
      "name":"lastPayout",
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
      "name":"myDividends",
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
      "name":"myTokens",
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
      "name":"players",
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
      "name":"reinvest",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"router",
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
         {
            "internalType":"uint256",
            "name":"_amountOfTokens",
            "type":"uint256"
         }
      ],
      "name":"sell",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"sellPrice",
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
            "name":"_customerAddress",
            "type":"address"
         }
      ],
      "name":"statsOf",
      "outputs":[
         {
            "internalType":"uint256[14]",
            "name":"",
            "type":"uint256[14]"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"sweep",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
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
         {
            "internalType":"address",
            "name":"_customerAddress",
            "type":"address"
         }
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
         
      ],
      "name":"tokenUniswapV2Router",
      "outputs":[
         {
            "internalType":"contract IUniswapV2Router02",
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
      "name":"totalBuyBack",
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
      "name":"totalClaims",
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
      "name":"totalDeposits",
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
      "name":"totalTokenBalance",
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
            "name":"_toAddress",
            "type":"address"
         },
         {
            "internalType":"uint256",
            "name":"_amountOfTokens",
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
         
      ],
      "name":"uniswapV2Router",
      "outputs":[
         {
            "internalType":"contract IUniswapV2Router02",
            "name":"",
            "type":"address"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"_tokenRouter",
            "type":"address"
         }
      ],
      "name":"updateTokenRouter",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"withdraw",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "stateMutability":"payable",
      "type":"receive"
   }
]

TRUNK_BACKED_POOL_CONTRACT_ADDRESS = "0xDb2c2741542E37bDa373bE49605cb8EFC5440455"
TRUNK_BACKED_POOL_ABI = [
   {
      "inputs":[
         
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
            "indexed":False,
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"balance",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onCredit",
      "type":"event"
   },
   {
      "anonymous":False,
      "inputs":[
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"amount",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"balance",
            "type":"uint256"
         },
         {
            "indexed":False,
            "internalType":"uint256",
            "name":"timestamp",
            "type":"uint256"
         }
      ],
      "name":"onDebit",
      "type":"event"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"pool",
            "type":"address"
         }
      ],
      "name":"add",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
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
         
      ],
      "name":"available",
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
      "name":"backedAddress",
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
      "name":"backedToken",
      "outputs":[
         {
            "internalType":"contract IERC20",
            "name":"",
            "type":"address"
         }
      ],
      "stateMutability":"view",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"pool",
            "type":"address"
         }
      ],
      "name":"contains",
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
         {
            "internalType":"uint256",
            "name":"collateralAmount",
            "type":"uint256"
         }
      ],
      "name":"credit",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"creditBalance",
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
            "name":"userTokens",
            "type":"uint256"
         },
         {
            "internalType":"uint256",
            "name":"tokenSupply",
            "type":"uint256"
         }
      ],
      "name":"dailyEstimate",
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
      "name":"getUnlockTime",
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
      "name":"lastSweep",
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
            "name":"time",
            "type":"uint256"
         }
      ],
      "name":"lock",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
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
      "name":"payoutThreshold",
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
            "name":"pool",
            "type":"address"
         }
      ],
      "name":"remove",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
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
         
      ],
      "name":"renounceOwnership",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         
      ],
      "name":"reserve",
      "outputs":[
         {
            "internalType":"contract IElephantReserve",
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
      "name":"sweep",
      "outputs":[
         
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
         
      ],
      "name":"unlock",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"uint256",
            "name":"threshold",
            "type":"uint256"
         }
      ],
      "name":"updatePayoutThreshold",
      "outputs":[
         
      ],
      "stateMutability":"nonpayable",
      "type":"function"
   },
   {
      "inputs":[
         {
            "internalType":"address",
            "name":"reserveAddress",
            "type":"address"
         }
      ],
      "name":"updateReserve",
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
   }
]