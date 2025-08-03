import json
import base64
import matplotlib.pyplot as plt
from biometric_stream_simulator import BiometricStreamSimulator
from entropy_analyzer import EntropyAnalyzer
from ecdsa import SigningKey, SECP256k1
from WatermarkEmbedder import WatermarkEmbedder
from VerificationInterface import VerificationInterface

# Setup key pair
signing_key = SigningKey.generate(curve=SECP256k1)
verifying_key = signing_key.get_verifying_key()

# Simulate biometric signal
sim = BiometricStreamSimulator(signal_type='PPG')
timestamps, values = sim.stream(duration=10)

# Analyze entropy
entropy = EntropyAnalyzer()
entropy_scores = []
for v in values:
    entropy.add_sample(v)
    entropy_scores.append(entropy.compute_entropy_score())
final_entropy_score = entropy_scores[-1]

# Generate signature for payload
payload = {
    "timestamp": int(timestamps[-1]),
    "entropy_score": final_entropy_score,
    "device_id": "HUMANTAG123"
}
payload_str = json.dumps(payload, separators=(',', ':'))
signature = base64.b64encode(signing_key.sign(payload_str.encode('utf-8'))).decode('utf-8')

# Embed payload
embedder = WatermarkEmbedder()
full_payload = embedder.generate_payload(final_entropy_score, signature)
embedded = embedder.embed_to_media(media_file="sample_video.mp4", payload=full_payload)

# Verify
verifier = VerificationInterface(verifying_key)
verification_result = verifier.verify_payload(full_payload)

# Output results
print("Embedded Payload:")
print(full_payload)
print("\nVerification Result:")
print(verification_result)

# Plot signal + entropy for visualization
plt.figure(figsize=(10, 5))
plt.plot(timestamps, values, label='PPG Signal', alpha=0.6)
plt.plot(timestamps, entropy_scores, label='Entropy Score', color='red', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Signal / Score')
plt.title('Simulated Biometric Signal with Entropy and Cryptographic Verification')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()