import hashlib
from functools import lru_cache
from typing import List, Dict, Any


@lru_cache(maxsize=1024)
def fast_hash_checksum(data: str) -> str:
    """Compute double SHA-256 hash checksum with LRU caching."""
    first_pass = hashlib.sha256(data.encode('utf-8')).digest()
    return hashlib.sha256(first_pass).hexdigest()[:8]


class TransactionProcessor:
    """Handles batch processing of cryptocurrency transactions with cached hashing."""

    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def validate_payload_batch(self, payloads: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate transaction payloads in optimized batches using memoized hashes."""
        results = []
        for item in payloads:
            raw_tx = f"{item.get('sender')}:{item.get('recipient')}:{item.get('amount')}"
            checksum = fast_hash_checksum(raw_tx)
            is_valid = item.get('amount', 0) > 0 and len(item.get('recipient', '')) > 0
            
            results.append({
                "tx_id": item.get("id"),
                "checksum": checksum,
                "valid": is_valid
            })
        return results

    def summarize_batch(self, processed_batch: List[Dict[str, Any]]) -> Dict[str, int]:
        """Aggregate summary metrics for processed batch."""
        valid_count = sum(1 for tx in processed_batch if tx["valid"])
        return {
            "total": len(processed_batch),
            "valid": valid_count,
            "invalid": len(processed_batch) - valid_count
        }
