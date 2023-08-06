import base64
import json
from typing import Any, Dict, List

import eth_keys


from icplazapy._wallet import DEFAULT_BECH32_HRP, privkey_to_address, privkey_to_pubkey
from icplazapy.typing import SyncMode


class Transaction:
    """A Cosmos transaction.

    After initialization, one or more token transfers can be added by
    calling the `add_transfer()` method. Finally, call `get_pushable()`
    to get a signed transaction that can be pushed to the `POST /txs`
    endpoint of the Cosmos REST API.
    """

    def __init__(
        self,
        *,
        privkey: bytes,
        account_num: int,
        sequence: int,
        fee: int,
        gas: int,
        fee_denom: str = "uict",
        memo: str = "",
        chain_id: str = "cosmoshub-4",
        hrp: str = DEFAULT_BECH32_HRP,
        sync_mode: SyncMode = "sync",
    ) -> None:
        self._privkey = privkey
        self._account_num = account_num
        self._sequence = sequence
        self._fee = fee
        self._fee_denom = fee_denom
        self._gas = gas
        self._memo = memo
        self._chain_id = chain_id
        self._hrp = hrp
        self._sync_mode = sync_mode
        self._msgs: List[dict] = []

    def add_transfer(self, recipient: str, amount: int, denom: str = "uict") -> None:
        transfer = {
            "type": "cosmos-sdk/MsgSend",
            "value": {
                "from_address": privkey_to_address(self._privkey, hrp=self._hrp),
                "to_address": recipient,
                "amount": [{"denom": denom, "amount": str(amount)}],
            },
        }
        self._msgs.append(transfer)

    def get_pushable(self) -> str:
        pubkey = privkey_to_pubkey(self._privkey, True)
        print(pubkey.hex())
        base64_pubkey = base64.b64encode(pubkey).decode("utf-8")
        pushable_tx = {
            "tx": {
                "msg": self._msgs,
                "fee": {
                    "gas": str(self._gas),
                    "amount": [{"denom": self._fee_denom, "amount": str(self._fee)}],
                },
                "memo": self._memo,
                "signatures": [
                    {
                        "signature": self._sign(),
                        "pub_key": {"type": "ethermint/PubKeyEthSecp256k1", "value": base64_pubkey},
                        # "pub_key": {"type": "tendermint/PubKeySecp256k1", "value": base64_pubkey},
                        # "account_number": str(self._account_num),
                        # "sequence": str(self._sequence),
                    }
                ],
            },
            "mode": self._sync_mode,
        }
        return json.dumps(pushable_tx, separators=(",", ":"))

    def _sign(self) -> str:
        message_str = json.dumps(self._get_sign_message(), separators=(",", ":"), sort_keys=True)
        message_bytes = message_str.encode("utf-8")
        mm = message_bytes

        signerPrivKey = eth_keys.keys.PrivateKey(self._privkey)
        signature = signerPrivKey.sign_msg(mm)

        print('Signature: [r = {0}, s = {1}, v = {2}]'.format(hex(signature.r), hex(signature.s), hex(signature.v)))

        signature_compact = hex(signature.r)[2:].zfill(64) + hex(signature.s)[2:].zfill(64) + hex(signature.v)[2:].zfill(2)

        print(signature_compact)

        signature_compact = bytes.fromhex(signature_compact)

        print(signature_compact.hex())

        signature_base64_str = base64.b64encode(signature_compact).decode("utf-8")
        return signature_base64_str

    def _get_sign_message(self) -> Dict[str, Any]:
        return {
            "chain_id": self._chain_id,
            "account_number": str(self._account_num),
            "fee": {
                "gas": str(self._gas),
                "amount": [{"amount": str(self._fee), "denom": self._fee_denom}],
            },
            "memo": self._memo,
            "sequence": str(self._sequence),
            "msgs": self._msgs,
        }
