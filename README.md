# wallet-utility-18

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

wallet-utility-18 is a Python command-line tool for cryptocurrency wallet operations. It handles mnemonic generation, address derivation, and transaction signing for Bitcoin and Ethereum without requiring external services.

## Features
- Generate BIP39 mnemonics and derive addresses using standard BIP44 paths for Bitcoin and Ethereum
- Sign Ethereum transactions and personal messages from raw inputs
- Import existing seeds or private keys and export data in JSON or WIF formats
- Validate addresses and derive multiple child keys in a single operation

## Installation

```bash
git clone https://github.com/Developer/wallet-utility-18.git
cd wallet-utility-18
pip install -r requirements.txt
pip install -e .
```

## Usage

Generate a new Ethereum wallet:

```bash
wallet-utility generate --coin eth
```

Sign a transaction:

```bash
wallet-utility sign-tx --network ethereum --private-key <key> --to 0x... --value 0.01
```