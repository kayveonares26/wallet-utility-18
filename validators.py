import re

def is_valid_ethereum_address(address: str) -> bool:
    """Validate Ethereum address format."""
    if not isinstance(address, str):
        return False
    # Strip 0x prefix
    if address.lower().startswith('0x'):
        address = address[2:]
    # Must be 40 hex characters
    if len(address) != 40:
        return False
    return bool(re.match(r'^[0-9a-fA-F]{40}$', address))

def is_valid_bitcoin_address(address: str) -> bool:
    """Basic validation for common Bitcoin address formats."""
    if not isinstance(address, str) or not address:
        return False
    # P2PKH starts with 1, P2SH with 3, Bech32 with bc1
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return True
    if re.match(r'^bc1[a-z0-9]{39,59}$', address.lower()):
        return True
    return False

def is_valid_private_key(private_key: str) -> bool:
    """Validate hex private key for 256-bit key."""
    if not isinstance(private_key, str):
        return False
    if private_key.lower().startswith('0x'):
        private_key = private_key[2:]
    if len(private_key) != 64:
        return False
    return bool(re.match(r'^[0-9a-fA-F]{64}$', private_key))

def validate_transaction_hash(tx_hash: str) -> bool:
    """Check if string is valid transaction hash."""
    if not isinstance(tx_hash, str):
        return False
    if tx_hash.lower().startswith('0x'):
        tx_hash = tx_hash[2:]
    if len(tx_hash) != 64:
        return False
    return bool(re.match(r'^[0-9a-fA-F]{64}$', tx_hash))

def is_positive_amount(amount: float) -> bool:
    """Ensure amount is positive number."""
    if not isinstance(amount, (int, float)):
        return False
    return amount > 0

def validate_wallet_balance(balance: float, required: float) -> bool:
    """Check if balance is sufficient."""
    if not isinstance(balance, (int, float)) or not isinstance(required, (int, float)):
        return False
    return balance >= required