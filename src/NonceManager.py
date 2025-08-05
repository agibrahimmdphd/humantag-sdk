import time
import random

class NonceManager:
    def get_nonce(self):
        # Simulates a unique, timestamp-based nonce
        return f"nonce_{int(time.time())}_{random.randint(1000,9999)}"

