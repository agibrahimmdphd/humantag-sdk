import json
import base64
from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

class VerificationInterface:
    def __init__(self, verifying_key: VerifyingKey):
        self.vk = verifying_key

    def verify_payload(self, payload_json):
        try:
            payload = json.loads(payload_json)
            signature = base64.b64decode(payload["signature"])
            stripped_payload = {
                "timestamp": payload["timestamp"],
                "entropy_score": payload["entropy_score"],
                "device_id": payload["device_id"]
            }
            message = json.dumps(stripped_payload, separators=(',', ':'))
            self.vk.verify(signature, message.encode('utf-8'))
            return {
                "verified": True,
                "timestamp": payload["timestamp"],
                "device_id": payload["device_id"],
                "entropy_score": payload["entropy_score"]
            }
        except (BadSignatureError, KeyError, ValueError, json.JSONDecodeError):
            return {"verified": False, "error": "Invalid payload or signature"}