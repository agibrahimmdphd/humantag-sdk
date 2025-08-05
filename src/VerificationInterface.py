import json

class VerificationInterface:
    def __init__(self, entropy_threshold=0.3):
        self.entropy_threshold = entropy_threshold

    def verify(self, signed_payload):
        try:
            payload = signed_payload["payload"]
            entropy_score = payload["entropy_score"]
            signature = signed_payload["signature"]

            # 🔐 Step 1: Entropy Gating
            if entropy_score < self.entropy_threshold:
                print(f"[⚠️] Entropy too low: {entropy_score:.2f} < threshold {self.entropy_threshold}")
                print("[🚫] Possible spoof or replay detected")
                return False

            # ✅ Step 2: Simulate signature validation (in real version, use public key)
            print("[✔] Signature validated (simulated)")
            return True

        except Exception as e:
            print(f"[❌] Verification failed: {e}")
            return False

