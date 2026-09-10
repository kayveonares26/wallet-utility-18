from typing import List, Dict, Optional

class WalletManager:
    def __init__(self, currency: str = "BTC") -> None:
        """Initialize the wallet manager with a default currency."""
        self.currency: str = currency
        self.balances: Dict[str, float] = {}

    def get_balance(self, address: str) -> float:
        """Retrieve balance for a specific crypto address."""
        return self.balances.get(address, 0.0)

    def update_balance(self, address: str, amount: float) -> None:
        """Update the balance for a given address."""
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.balances[address] = amount

    def get_active_addresses(self) -> List[str]:
        """Return a list of all addresses with positive balances."""
        return [addr for addr, bal in self.balances.items() if bal > 0]

    def calculate_total(self) -> float:
        """Calculate the sum of all stored balances."""
        return sum(self.balances.values())

    def reset_wallet(self, address: Optional[str] = None) -> None:
        """Clear balances for a specific address or all."""
        if address:
            self.balances.pop(address, None)
        else:
            self.balances.clear()