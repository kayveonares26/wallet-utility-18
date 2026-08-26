"""
Global constants for wallet-utility-18.
Handles network configurations and transaction limits.
"""

# Network identifiers
NETWORKS = {
    "mainnet": "https://api.mainnet.crypto.org",
    "testnet": "https://api.testnet.crypto.org",
    "devnet": "http://localhost:8545"
}

# Supported cryptocurrency ticker symbols
SUPPORTED_CURRENCIES = [
    "BTC",
    "ETH",
    "USDT",
    "SOL",
    "ADA"
]

# Transaction safety limits
MAX_TRANSACTION_FEE_GWEI = 500
MIN_CONFIRMATIONS_REQUIRED = 3

# Gas estimation parameters
DEFAULT_GAS_LIMIT = 21000
GAS_BUFFER_PERCENTAGE = 10

# Error message strings
ERR_INVALID_ADDRESS = "Invalid wallet address format provided."
ERR_INSUFFICIENT_FUNDS = "Insufficient balance to cover transaction and fees."
ERR_NETWORK_TIMEOUT = "Connection to the crypto network timed out."
