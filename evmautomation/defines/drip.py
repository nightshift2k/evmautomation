DRIP_FAUCET_CONTRACT_ADDRESS = "0xFFE811714ab35360b67eE195acE7C10D93f89D8C"
DRIP_FAUCET_ABI = [
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "_src",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "_dest",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_deposits",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "_payouts",
        "type": "uint256"
      }
    ],
    "name": "BalanceTransfer",
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
        "indexed": True,
        "internalType": "address",
        "name": "beneficiary",
        "type": "address"
      }
    ],
    "name": "BeneficiaryUpdate",
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
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "name": "Checkin",
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
        "indexed": True,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "DirectPayout",
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
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "name": "HeartBeat",
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
        "name": "interval",
        "type": "uint256"
      }
    ],
    "name": "HeartBeatIntervalUpdate",
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
        "name": "referrals",
        "type": "uint256"
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
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "total_structure",
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
        "indexed": True,
        "internalType": "address",
        "name": "manager",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "name": "ManagerUpdate",
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
        "indexed": True,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "MatchPayout",
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
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "name": "NewAirdrop",
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
        "indexed": True,
        "internalType": "address",
        "name": "upline",
        "type": "address"
      }
    ],
    "name": "Upline",
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
