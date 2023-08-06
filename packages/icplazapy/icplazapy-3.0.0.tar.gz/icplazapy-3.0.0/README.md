
[![PyPI version](https://img.shields.io/pypi/v/icplazapy)](https://pypi.org/project/icplazapy)

# icplazapy
- forked from [hukkin/cosmospy](https://github.com/hukkin/cosmospy)
- modified [hukkin/cosmospy](https://github.com/hukkin/cosmospy) to icplazapy
- icplaza chain is an evmos like chain.
<!--- Don't edit the version line below manually. Let bump2version do it for you. -->

> Version 3.0.0

> Tools for Icplaza wallet management and offline transaction signing

**Table of Contents**  *generated with [mdformat-toc](https://github.com/hukkin/mdformat-toc)*

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Installing](#installing)
- [Usage](#usage)
  - [Generating a wallet](#generating-a-wallet)
  - [Converter functions](#converter-functions)
    - [Mnemonic seed to private key](#mnemonic-seed-to-private-key)
    - [Private key to public key](#private-key-to-public-key)
    - [Public key to address](#public-key-to-address)
    - [Private key to address](#private-key-to-address)
    - [Public key to hex address](#public-key-to-hex-address)
    - [Private key to hex address](#private-key-to-hex-address)
    - [address from hex address](#address-from-hex-address)
    - [address to hex address](#address-to-hex-address)
  - [Signing transactions](#signing-transactions)

<!-- mdformat-toc end -->

## Installing<a name="installing"></a>

Installing from PyPI repository (https://pypi.org/project/icplazapy):

```bash
pip install icplazapy
```

## Usage<a name="usage"></a>

### Generating a wallet<a name="generating-a-wallet"></a>

```python
from icplazapy import generate_wallet

wallet = generate_wallet()
```

The value assigned to `wallet` will be a dictionary just like:

```python
{
    'seed': 'loan weapon tone clever party picture spot novel almost change rug primary speak entry usage maximum farm beyond magnet crazy later day addict orchard', 
    'derivation_path': "m/44'/118'/0'/0/0", 
    'private_key': b'\x06\xe5*di\x88q0\xe4\x08Y\x9aL\xcb\xd7\xc0\xac\xc6\x9d\x9a\x18\xc5$\x00\xacM5\xae\x1b\x07\xe7N', 'public_key': b'\x02Jj\xe8>y\xe0\xcb\xe2\x11oIX@29p\xd3\x1c\x83\xcd\xa4i\xb0\x9e\xd7\x9f!\xf5\xbe\xb7\xe1i', 
    'address': 'icplaza1ayuhuzmlkw3dr7ftajxcl9kzg4vvzr0ltwpwjl'
}
```

### Converter functions<a name="converter-functions"></a>

#### Mnemonic seed to private key<a name="mnemonic-seed-to-private-key"></a>

```python
from icplazapy import BIP32DerivationError, seed_to_privkey

seed = (
    "teach there dream chase fatigue abandon lava super senior artefact close upgrade"
)
try:
    privkey = seed_to_privkey(seed, path="m/44'/118'/0'/0/0")
except BIP32DerivationError:
    print("No valid private key in this derivation path!")
```

#### Private key to public key<a name="private-key-to-public-key"></a>

```python
from icplazapy import privkey_to_pubkey

privkey = bytes.fromhex(
    "6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa"
)
pubkey = privkey_to_pubkey(privkey)
```

#### Public key to address<a name="public-key-to-address"></a>

```python
from icplazapy import pubkey_to_address

pubkey = bytes.fromhex(
    "03e8005aad74da5a053602f86e3151d4f3214937863a11299c960c28d3609c4775"
)
addr = pubkey_to_address(pubkey)
```

#### Private key to address<a name="private-key-to-address"></a>

```python
from icplazapy import privkey_to_address

privkey = bytes.fromhex(
    "6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa"
)
addr = privkey_to_address(privkey)
```
#### Public key to hex address<a name="pubkey-to-hex-address"></a>

```python
from icplazapy import pubkey_to_hex_address

pubkey = bytes.fromhex(
    "03e8005aad74da5a053602f86e3151d4f3214937863a11299c960c28d3609c4775"
)
addr = pubkey_to_address(pubkey)
```
#### Private key to hex address<a name="privkey-to-hex-address"></a>
```python
from icplazapy import privkey_to_hex_address

privkey = bytes.fromhex(
    "6dcd05d7ac71e09d3cf7da666709ebd59362486ff9e99db0e8bc663570515afa"
)
addr = privkey_to_address(privkey)
```
#### address from hex address<a name="address-from-hex-address"></a>
```python
from icplazapy import from_hex_address
hex_addr = "0x4790155804CB6fd0D3697CBb367E75397408a587"
addr = from_hex_address(hex_addr)
```
#### address to hex address<a name="address-to-hex-address"></a>
```python
from icplazapy import to_hex_address
addr = "icplaza1g7gp2kqyedhap5mf0janvln4896q3fv87z2dm6"
hex_addr = to_hex_address(addr)
```


### Signing transactions<a name="signing-transactions"></a>

```python
from icplazapy import Transaction

tx = Transaction(
    privkey=bytes.fromhex(
        "26d167d549a4b2b66f766b0d3f2bdbe1cd92708818c338ff453abde316a2bd59"
    ),
    account_num=11335,
    sequence=0,
    fee=1000,
    gas=70000,
    memo="",
    chain_id="icplaza_9000-4",
    sync_mode="sync",
)
tx.add_transfer(
    recipient="icplaza1g7gp2kqyedhap5mf0janvln4896q3fv87z2dm6", amount=387000
)

pushable_tx = tx.get_pushable()


# Optionally submit the transaction using your preferred method.
# This example uses the httpx library.
import httpx

# icplaza rest api
api_base_url = ""
httpx.post(api_base_url + "/txs", data=pushable_tx)
```

One or more token transfers can be added to a transaction by calling the `add_transfer` method.

When the transaction is fully prepared, calling `get_pushable` will return a signed transaction in the form of a JSON string.
This can be used as request body when calling the `POST /txs` endpoint of the [Cosmos REST API](https://cosmos.network/rpc).
