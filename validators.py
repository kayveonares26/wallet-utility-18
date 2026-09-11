import re

class WalletValidationError(ValueError):
    """Custom exception for wallet validation errors."""
    pass

class CryptoValidator:
    """Validator for cryptocurrency addresses and transaction parameters."""

    BTC_ADDRESS_RE = re.compile(r'^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[ac-hj-np-z0-9]{11,71})$')
    ETH_ADDRESS_RE = re.compile(r'^0x[a-fA-F0-9]{40}$')

    @classmethod
    def validate_address(cls, address: str, asset: str) -> bool:
        """Validates cryptocurrency address based on asset type."""
        clean_address = address.strip()
        asset_upper = asset.upper()
        
        if asset_upper == 'BTC':
            if not cls.BTC_ADDRESS_RE.match(clean_address):
                raise WalletValidationError(f"Invalid BTC address format: {address}")
        elif asset_upper == 'ETH':
            if not cls.ETH_ADDRESS_RE.match(clean_address):
                raise WalletValidationError(f"Invalid ETH address format: {address}")
        else:
            raise WalletValidationError(f"Unsupported asset type: {asset}")
        return True

    @classmethod
    def validate_amount(cls, amount: float, min_amount: float = 0.0001) -> bool:
        """Validates transaction amount is positive and above minimum threshold."""
        try:
            val = float(amount)
        except (ValueError, TypeError):
            raise WalletValidationError(f"Amount must be a valid number, got {amount}")
            
        if val <= 0:
            raise WalletValidationError("Transaction amount must be greater than zero")
        if val < min_amount:
            raise WalletValidationError(f"Amount {val} is below minimum allowed {min_amount}")
        return True