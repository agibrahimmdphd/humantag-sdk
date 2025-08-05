import json
from ecdsa import SigningKey, NIST256p

class SignatureEngine:
    def __init__(self):
        self.sk = SigningKey.generate(curve=NIST256p)

    def sign(self, payload_dict):
        # Convert dict to a consistent byte representation (JSON)
        msg = json.dumps(payload_dict, sort_keys=True).encode('utf-8')
        signature = self.sk.sign(msg)
        return {
            "payload": payload_dict,
            "signature": signature.hex()
        }

