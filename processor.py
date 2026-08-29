import json
from collections import defaultdict
from typing import List, Dict, Any

def clean_address(address: str) -> str:
    """Remove whitespace and standardize wallet address."""
    return address.strip().lower()

def is_valid_address(address: str) -> bool:
    """Check if address is a valid 42-char hex ethereum address."""
    if not address or not address.startswith("0x"):
        return False
    hex_part = address[2:]
    return len(hex_part) == 40 and all(c in "0123456789abcdef" for c in hex_part)

def process_transactions(transactions: List[Dict[str, Any]]) -> Dict[str, float]:
    """Aggregate balances from list of transactions."""
    balances: Dict[str, float] = defaultdict(float)
    for tx in transactions:
        sender = clean_address(tx.get("from", ""))
        receiver = clean_address(tx.get("to", ""))
        amount = float(tx.get("amount", 0.0))
        if is_valid_address(sender):
            balances[sender] -= amount
        if is_valid_address(receiver):
            balances[receiver] += amount
    return dict(balances)

def reorganize_wallet_data(raw_wallets: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Reorganize raw data into cleaned wallet summaries."""
    organized: Dict[str, Dict[str, Any]] = {}
    for wallet_info in raw_wallets:
        addr = clean_address(wallet_info.get("address", ""))
        if not is_valid_address(addr):
            continue
        tx_list = wallet_info.get("transactions", [])
        balance_summary = process_transactions(tx_list)
        total_balance = balance_summary.get(addr, 0.0)
        organized[addr] = {
            "balance": total_balance,
            "transaction_count": len(tx_list),
            "cleaned_address": addr
        }
    return organized

# Example usage for testing the processor
if __name__ == "__main__":
    sample_raw_data = [
        {
            "address": " 0x742d35Cc6634C0532925a3b844Bc454e4438f44e ",
            "transactions": [
                {"from": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "to": "0x1234567890123456789012345678901234567890", "amount": 2.5},
                {"from": "0x1234567890123456789012345678901234567890", "to": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", "amount": 1.0}
            ]
        }
    ]
    result = reorganize_wallet_data(sample_raw_data)
    print(json.dumps(result, indent=2))