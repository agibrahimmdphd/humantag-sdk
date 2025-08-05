# API Specification

This document outlines the structure and usage of the HumanTag SDK.

---

## Modules and Functions

### 1. biometric_stream_simulator.py
```python
generate_biometric_stream()
```
Generates mock biometric data (PPG, GSR, EKG).

---

### 2. entropy_analyzer.py
```python
analyze_entropy(signal: dict) -> float
```
Computes entropy score based on incoming signal.

---

### 3. SignatureEngine.py
```python
class SignatureEngine:
    def sign(payload: dict) -> str
    def verify(payload: dict, signature: str) -> bool
```
Handles ECDSA signing and verification.

---

### 4. WatermarkEmbedder.py
```python
embed_watermark(filename: str, tag: str) -> str
```
Simulates watermarking by tagging a file.

---

### 5. EncryptionUtils.py
```python
encrypt_payload(payload: dict) -> str
decrypt_payload(payload_str: str) -> dict
```
Basic encryption/decryption stub for demonstration.

---

### 6. VerificationInterface.py
```python
verify_biometric_payload(payload: dict, signature: str) -> bool
```
Unified SDK verification handler.

---

## Sample Usage
See `examples/demo_full_pipeline_verbose.py` for integration example.
