import time
from functools import lru_cache
from typing import Dict, Any, List

class TransactionProcessor:
    def __init__(self, cache_size: int = 1024) -> None:
        self.cache_size = cache_size

    @lru_cache(maxsize=1024)
    def compute_weighted_fee(self, gas_limit: int, gas_price: int, multiplier: float) -> float:
        """Calculate optimized transaction fee with memoization."""
        base_fee = gas_limit * gas_price
        return round(base_fee * multiplier, 8)

    def batch_process_wallets(self, wallet_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process wallet transactions in optimized batches."""
        results = []
        start_time = time.perf_counter()
        
        for item in wallet_data:
            limit = item.get("gas_limit", 21000)
            price = item.get("gas_price", 1000000000)
            mult = item.get("multiplier", 1.1)
            
            fee = self.compute_weighted_fee(limit, price, mult)
            results.append({
                "address": item.get("address"),
                "calculated_fee": fee,
                "processed_at": time.time()
            })
            
        execution_time = time.perf_counter() - start_time
        print(f"Processed {len(results)} wallets in {execution_time:.6f} seconds")
        return results
