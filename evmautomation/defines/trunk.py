# TRUNK token
TRUNK_TOKEN_CONTRACT_ADDRESS = "0xdd325C38b12903B727D16961e61333f4871A70E0"

# ELEPHANT token
ELEPHANT_TOKEN_CONTRACT_ADDRESS = "0xE283D0e3B8c102BAdF5E8166B73E02D96d92F688"

# FlowEngine aka Stampede
# old:
# TRUNK_STAMPEDE_CONTRACT_ADDRESS = "0x6839e295a8f13864A2830fA0dCC0F52e71a82DbF"
# new:    
TRUNK_STAMPEDE_CONTRACT_ADDRESS = "0x3685407AabF9A0Ab54Ed39168733B1e2D2A80e5E"
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
				"internalType": "bool",
				"name": "paused",
				"type": "bool"
			}
		],
		"name": "RunStatusUpdated",
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
			}
		],
		"name": "UpdateFlowData",
		"type": "event"
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
		"name": "UpdatePeanutRaffleBonus",
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
			}
		],
		"name": "UpdateRaffle",
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
			}
		],
		"name": "UpdateReferralData",
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
			}
		],
		"name": "UpdateReserve",
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
			}
		],
		"name": "UpdateSponsorData",
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
		"name": "collateralTreasury",
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
		"name": "peanutBonus",
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
				"name": "_amount",
				"type": "uint256"
			}
		],
		"name": "peanuts",
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
		"name": "peggedPayoutOf",
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
		"name": "raffle",
		"outputs": [
			{
				"internalType": "contract IRaffle",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
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
		"outputs": [
			{
				"internalType": "uint256",
				"name": "_rolledAmount",
				"type": "uint256"
			}
		],
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
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "scaleBusdByPeg",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "scaledAmount",
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
		"name": "scaleByPeg",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "scaledAmount",
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
				"internalType": "uint256",
				"name": "bonus",
				"type": "uint256"
			}
		],
		"name": "updatePeanutRaffleBonus",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "raffleAddress",
				"type": "address"
			}
		],
		"name": "updateRaffle",
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
				"internalType": "bool",
				"name": "paused",
				"type": "bool"
			}
		],
		"name": "updateRunStatus",
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

# native staking pool
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

# TRUNK reserver for redeeming
TRUNK_RESERVE_CONTRACT_ADDRESS = "0xE9BCD0228Af9719dB4518De40060FAd585d5f3f9"
# TRUNK_RESERVE_CONTRACT_ADDRESS = "0xD520a3B47E42a1063617A9b6273B206a07bDf834"
TRUNK_RESERVE_ABI = [
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
             "indexed":False,
             "internalType":"uint256",
             "name":"creditAmount",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"coreAmount",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"adjustedCoreAmount",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"coreAdjustedCreditAmount",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"address",
             "name":"destination",
             "type":"address"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"timestamp",
             "type":"uint256"
          }
       ],
       "name":"onCreditRedemption",
       "type":"event"
    },
    {
       "anonymous":False,
       "inputs":[
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"collateral",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"minted",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"fee",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"credits",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"timestamp",
             "type":"uint256"
          }
       ],
       "name":"onMint",
       "type":"event"
    },
    {
       "anonymous":False,
       "inputs":[
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"minted",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"collateral",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"fee",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"core",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"adjustedCore",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"credits",
             "type":"uint256"
          },
          {
             "indexed":False,
             "internalType":"bool",
             "name":"isPartner",
             "type":"bool"
          },
          {
             "indexed":False,
             "internalType":"uint256",
             "name":"timestamp",
             "type":"uint256"
          }
       ],
       "name":"onRedemption",
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
          
       ],
       "name":"antiSlippageFactor",
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
       "name":"backedPool",
       "outputs":[
          {
             "internalType":"contract IRewardPool",
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
       "name":"collateralAddress",
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
       "name":"collateralFactor",
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
       "name":"collateralRouter",
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
       "name":"collateralTreasury",
       "outputs":[
          {
             "internalType":"contract ITreasury",
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
       "name":"collateralTreasuryAddress",
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
       "name":"collateralizationRatio",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"cratio",
             "type":"uint256"
          }
       ],
       "stateMutability":"view",
       "type":"function"
    },
    {
       "inputs":[
          
       ],
       "name":"collateralizationRatioLP",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"cratio",
             "type":"uint256"
          }
       ],
       "stateMutability":"view",
       "type":"function"
    },
    {
       "inputs":[
          
       ],
       "name":"coreAddress",
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
       "name":"coreTreasury",
       "outputs":[
          {
             "internalType":"contract ITreasury",
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
       "name":"coreTreasuryAddress",
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
       "name":"distributionFactor",
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
             "name":"collateralAmount",
             "type":"uint256"
          }
       ],
       "name":"estimateCollateralToCore",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"wethAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAmount",
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
             "name":"coreAmount",
             "type":"uint256"
          }
       ],
       "name":"estimateCoreToCollateral",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"wethAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"collateralAmount",
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
             "name":"collateralAmount",
             "type":"uint256"
          }
       ],
       "name":"estimateMint",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"backedAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
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
             "name":"backedAmount",
             "type":"uint256"
          }
       ],
       "name":"estimateRedemption",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"collateralAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"adjustedCoreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAdjustedCreditAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"totalCollateralValue",
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
             "name":"backedAmount",
             "type":"uint256"
          }
       ],
       "name":"estimateRedemptionV2",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"collateralAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"adjustedCoreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAdjustedCreditAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"totalCollateralValue",
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
       "name":"liquidityThreshold",
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
          {
             "internalType":"uint256",
             "name":"collateralAmount",
             "type":"uint256"
          }
       ],
       "name":"mint",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"backedAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
             "type":"uint256"
          }
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
       "name":"partnerAddress",
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
       "name":"performancePool",
       "outputs":[
          {
             "internalType":"contract IRewardPool",
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
       "name":"processingFee",
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
             "name":"backedAmount",
             "type":"uint256"
          }
       ],
       "name":"redeem",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"collateralAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"adjustedCoreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
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
             "name":"collateralAmount",
             "type":"uint256"
          }
       ],
       "name":"redeemCollateralCreditToWETH",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"wethAmount",
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
             "name":"destination",
             "type":"address"
          },
          {
             "internalType":"uint256",
             "name":"creditAmount",
             "type":"uint256"
          }
       ],
       "name":"redeemCredit",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"coreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"adjustedCoreAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"coreAdjustedCreditAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
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
             "name":"destination",
             "type":"address"
          },
          {
             "internalType":"uint256",
             "name":"creditAmount",
             "type":"uint256"
          }
       ],
       "name":"redeemCreditAsBacked",
       "outputs":[
          {
             "internalType":"uint256",
             "name":"backedAmount",
             "type":"uint256"
          },
          {
             "internalType":"uint256",
             "name":"feeAmount",
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
       "name":"router",
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
       "name":"routerAddress",
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
       "name":"slippageRate",
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
             "name":"antislippage",
             "type":"uint256"
          }
       ],
       "name":"updateAntiSlippageFactor",
       "outputs":[
          
       ],
       "stateMutability":"nonpayable",
       "type":"function"
    },
    {
       "inputs":[
          {
             "internalType":"address",
             "name":"_router",
             "type":"address"
          }
       ],
       "name":"updateCollateralRouter",
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
       "name":"updateLiquidityThreshold",
       "outputs":[
          
       ],
       "stateMutability":"nonpayable",
       "type":"function"
    },
    {
       "inputs":[
          {
             "internalType":"address",
             "name":"backedRewardPoolAddress",
             "type":"address"
          },
          {
             "internalType":"address",
             "name":"performanceRewardPoolAddress",
             "type":"address"
          }
       ],
       "name":"updateRewardPools",
       "outputs":[
          
       ],
       "stateMutability":"nonpayable",
       "type":"function"
    },
    {
       "inputs":[
          {
             "internalType":"uint256",
             "name":"_rate",
             "type":"uint256"
          }
       ],
       "name":"updateSlippageRate",
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