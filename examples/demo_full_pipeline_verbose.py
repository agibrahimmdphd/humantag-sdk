import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import biometric_stream_simulator
import entropy_analyzer
from SignatureEngine import SignatureEngine
from WatermarkEmbedder import WatermarkEmbedder
from VerificationInterface import VerificationInterface
from EncryptionUtils import encrypt_payload, decrypt_payload
from NonceManager import NonceManager
import json
import time

# Step 1: Simulate biometric signal
signal = biometric_stream_simulator.generate_biometric_stream()
print(f"[✔] Biometric Signal: {signal}")

# Step 2: Entropy analysis
entropy_score = entropy_analyzer.analyze_entropy(signal)
print(f"[✔] Entropy Score: {entropy_score:.2f}")

# Step 3: Generate signed payload
signature_engine = SignatureEngine()
nonce_mgr = NonceManager()
nonce = nonce_mgr.get_nonce()
timestamp = time.time()

payload = {
    "device_id": "HT-001",
    "entropy_score": entropy_score,
    "timestamp": timestamp,
    "nonce": nonce,
    "signal": signal
}

# Step 4: Sign payload
signed_payload = signature_engine.sign(payload)
print(f"[✔] Signature: {signed_payload['signature'][:50]}...")

# Step 5: Encrypt payload
encrypted = encrypt_payload(signed_payload)
print(f"[✔] Encrypted Payload: {str(encrypted)[:60]}...")

# Step 6: Simulate watermark embedding
embedder = WatermarkEmbedder()
watermarked = embedder.embed(encrypted)
print(f"[✔] Watermark Embedded")

# Step 7: Verification
verifier = VerificationInterface()
decrypted = decrypt_payload(watermarked)
result = verifier.verify(decrypted)

print(f"[✔] Verification Result: {'✅ Verified = True' if result else '❌ Verification Failed'}")