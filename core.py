import re
import secrets
import hashlib
from decimal import Decimal

def validate_address(address: str) -> bool:
    """Check if address follows Ethereum format."""
    if not address or not address.startswith('0x'):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def wei_to_ether(wei_amount: int) -> Decimal:
    """Convert wei to ether using Decimal for precision."""
    if wei_amount < 0:
        raise ValueError('Amount cannot be negative')
    return Decimal(wei_amount) / Decimal(10**18)

def ether_to_wei(ether_amount: float) -> int:
    """Convert ether to wei."""
    if ether_amount < 0:
        raise ValueError('Amount cannot be negative')
    return int(Decimal(str(ether_amount)) * Decimal(10**18))

def generate_private_key() -> str:
    """Generate a secure random private key hex."""
    return '0x' + secrets.token_hex(32)

def compute_transaction_hash(tx_data: bytes) -> str:
    """Compute SHA256 hash of transaction data."""
    return hashlib.sha256(tx_data).hexdigest()

def format_token_amount(amount: int, decimals: int = 18) -> str:
    """Format token amount with decimals."""
    if amount == 0:
        return '0'
    value = Decimal(amount) / Decimal(10 ** decimals)
    return f'{value:.8f}'.rstrip('0').rstrip('.')

def is_valid_private_key(key: str) -> bool:
    """Validate private key length and hex."""
    if not key.startswith('0x'):
        return False
    key = key[2:]
    return len(key) == 64 and all(c in '0123456789abcdefABCDEF' for c in key)

def calculate_gas_cost(gas_limit: int, gas_price: int) -> int:
    """Calculate total gas cost in wei."""
    return gas_limit * gas_price