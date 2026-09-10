import re

# Common crypto address and key patterns
ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")
BTC_ADDRESS_PATTERN = re.compile(
    r"^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[ac-hj-np-z0-9]{11,71})$"
)
HEX_PRIVATE_KEY_PATTERN = re.compile(r"^[a-fA-F0-9]{64}$")

def is_valid_ethereum_address(address: str) -> bool:
    """Validates standard Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))

def is_valid_bitcoin_address(address: str) -> bool:
    """Validates basic Bitcoin address formats (Legacy, SegWit, Bech32)."""
    if not isinstance(address, str):
        return False
    return bool(BTC_ADDRESS_PATTERN.match(address))

def is_valid_hex_private_key(private_key: str) -> bool:
    """Validates if a private key is a valid 64-character hex string."""
    if not isinstance(private_key, str):
        return False
    clean_key = private_key[2:] if private_key.startswith("0x") else private_key
    return bool(HEX_PRIVATE_KEY_PATTERN.match(clean_key))

def is_valid_mnemonic_phrase(mnemonic: str) -> bool:
    """Validates basic structure and word count of a BIP-39 mnemonic phrase."""
    if not isinstance(mnemonic, str):
        return False
    words = mnemonic.strip().split()
    return len(words) in {12, 15, 18, 21, 24}
