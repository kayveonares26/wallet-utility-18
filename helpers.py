from decimal import Decimal, getcontext
import re
from typing import Union

# Set high precision for crypto calculations
getcontext().prec = 28

ETH_DECIMALS = 18
BTC_DECIMALS = 8

def wei_to_ether(wei: int) -> Decimal:
    '''Convert Wei (int) to Ether (Decimal).'''
    if not isinstance(wei, int) or wei < 0:
        raise ValueError('Wei value must be a non-negative integer.')
    return Decimal(wei) / Decimal(10 ** ETH_DECIMALS)

def ether_to_wei(ether: Union[Decimal, float, str, int]) -> int:
    '''Convert Ether to Wei (int) accurately using Decimal.'''
    ether_dec = Decimal(str(ether))
    if ether_dec < 0:
        raise ValueError('Ether value must be non-negative.')
    return int(ether_dec * Decimal(10 ** ETH_DECIMALS))

def satoshi_to_btc(satoshi: int) -> Decimal:
    '''Convert Satoshi (int) to BTC (Decimal).'''
    if not isinstance(satoshi, int) or satoshi < 0:
        raise ValueError('Satoshi value must be a non-negative integer.')
    return Decimal(satoshi) / Decimal(10 ** BTC_DECIMALS)

def btc_to_satoshi(btc: Union[Decimal, float, str, int]) -> int:
    '''Convert BTC to Satoshi (int) accurately using Decimal.'''
    btc_dec = Decimal(str(btc))
    if btc_dec < 0:
        raise ValueError('BTC value must be non-negative.')
    return int(btc_dec * Decimal(10 ** BTC_DECIMALS))

def validate_ethereum_address(address: str) -> bool:
    '''Validate Ethereum hex address pattern.'''
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))
