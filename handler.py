import hashlib
import json
from typing import Any, Dict, Optional, Tuple


class WalletTransactionHandler:
    """Handles parsing, validation, and hash generation for crypto wallet transactions."""

    def __init__(self, chain_id: int = 1, default_gas_limit: int = 21000) -> None:
        """Initialize handler with chain parameters.

        Args:
            chain_id: EVM network chain identifier.
            default_gas_limit: Fallback gas limit for standard transactions.
        """
        self.chain_id = chain_id
        self.default_gas_limit = default_gas_limit

    def prepare_transaction(
        self,
        to_address: str,
        value_wei: int,
        nonce: int,
        gas_price_gwei: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Construct a standard transaction payload dictionary.

        Args:
            to_address: Hex-encoded recipient wallet address.
            value_wei: Transaction amount in Wei.
            nonce: Sender account nonce.
            gas_price_gwei: Optional gas price in Gwei.

        Returns:
            Dictionary formatted as standard transaction parameters.
        """
        gas_price = (
            int(gas_price_gwei * 10**9)
            if gas_price_gwei is not None
            else 20 * 10**9
        )

        return {
            "to": to_address.lower(),
            "value": value_wei,
            "nonce": nonce,
            "gas": self.default_gas_limit,
            "gasPrice": gas_price,
            "chainId": self.chain_id,
        }

    def compute_tx_hash(self, tx_payload: Dict[str, Any]) -> str:
        """Calculate deterministically sorted SHA-256 hash of transaction data.

        Args:
            tx_payload: Structured transaction payload.

        Returns:
            Hex string prefixed with '0x' representing the payload hash.
        """
        serialized = json.dumps(tx_payload, sort_keys=True).encode("utf-8")
        raw_hash = hashlib.sha256(serialized).hexdigest()
        return f"0x{raw_hash}"

    def validate_address_format(self, address: str) -> Tuple[bool, str]:
        """Check if an address conforms to EVM hex address standard.

        Args:
            address: Address string to validate.

        Returns:
            Tuple containing boolean status and validation reason.
        """
        if not address.startswith("0x"):
            return False, "missing 0x prefix"
        if len(address) != 42:
            return False, "invalid address length"
        try:
            int(address[2:], 16)
        except ValueError:
            return False, "non-hexadecimal characters present"

        return True, "valid address format"
