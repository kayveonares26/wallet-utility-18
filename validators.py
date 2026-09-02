import re
from functools import lru_cache
from typing import List, Dict, Optional

# Pre-compiled regex patterns for fast matching across calls
ETH_REGEX = re.compile('^0x[a-fA-F0-9]{40}$')
BTC_REGEX = re.compile('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
SOL_REGEX = re.compile('^[1-9A-HJ-NP-Za-km-z]{32,44}$')

CHAIN_VALIDATORS = {
    'eth': ETH_REGEX,
    'btc': BTC_REGEX,
    'sol': SOL_REGEX
}

@lru_cache(maxsize=512)
def is_valid_address(address: str, chain: str = 'eth') -> bool:
    if not isinstance(address, str):
        return False
    regex = CHAIN_VALIDATORS.get(chain)
    if regex is None:
        return False
    return bool(regex.match(address))

def batch_validate(addresses: List[str], chain: str = 'eth') -> Dict[str, bool]:
    '''Batch validation for improved performance on multiple addresses.'''
    return {address: is_valid_address(address, chain) for address in addresses}

def filter_valid(addresses: List[str], chain: str = 'eth') -> List[str]:
    return [a for a in addresses if is_valid_address(a, chain)]

def detect_chain(address: str) -> Optional[str]:
    if not isinstance(address, str):
        return None
    if address.startswith('0x') and len(address) == 42:
        return 'eth'
    elif address[0] in ('1', '3') and 26 <= len(address) <= 35:
        return 'btc'
    elif 32 <= len(address) <= 44:
        return 'sol'
    return None