import hashlib
import functools
from typing import List, Dict, Set

@functools.lru_cache(maxsize=512)
def _hash_data(data: str) -> str:
    """Compute SHA256 hash with caching for performance"""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def derive_address(seed: str, path: str) -> str:
    """Derive wallet address from seed and derivation path"""
    combined = f"{seed}{path}"
    hash_val = _hash_data(combined)
    return "0x" + hash_val[:40]

def batch_derive_addresses(seeds: List[str], paths: List[str]) -> Dict[str, str]:
    """Batch derive addresses efficiently using cached hashes"""
    addresses = {}
    for seed in seeds:
        for path in paths:
            key = f"{seed}:{path}"
            addresses[key] = derive_address(seed, path)
    return addresses

def filter_unique_addresses(addresses: List[str]) -> Set[str]:
    """Use set for O(1) lookups and deduplication"""
    return set(addresses)

def compute_total_balance(balances: Dict[str, float]) -> float:
    """Optimized balance summation"""
    return sum(balances.values())

def validate_and_cache(addresses: List[str]) -> List[str]:
    """Validate list of addresses"""
    valid = []
    for addr in addresses:
        if len(addr) == 42 and addr.startswith("0x"):
            try:
                int(addr[2:], 16)
                valid.append(addr)
            except:
                pass
    return valid

def optimize_transaction_list(transactions: List[Dict]) -> List[Dict]:
    """Sort and dedup transactions for performance"""
    seen = set()
    unique = []
    for tx in sorted(transactions, key=lambda x: x.get('timestamp', 0)):
        tx_id = tx.get('id')
        if tx_id and tx_id not in seen:
            seen.add(tx_id)
            unique.append(tx)
    return unique