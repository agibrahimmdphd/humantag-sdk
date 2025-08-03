# HumanTag SDK – API Specification

## BiometricStreamSimulator

```python
BiometricStreamSimulator(signal_type: str = 'PPG', noise_level: float = 0.05)
.stream(duration: int = 10) -> (timestamps: List[float], values: List[float])
```

## EntropyAnalyzer

```python
EntropyAnalyzer(window_size: int = 10)
.add_sample(value: float)
.compute_entropy_score() -> float
```

## WatermarkEmbedder

```python
WatermarkEmbedder(device_id: str = "HUMANTAG123")
.generate_payload(entropy_score: float, signature: str) -> str
.embed_to_media(media_file: str, payload: str) -> dict
```

## VerificationInterface

```python
VerificationInterface(verifying_key: ecdsa.VerifyingKey)
.verify_payload(payload_json: str) -> dict
```

Returns:
- `verified: bool`
- `timestamp: int`
- `device_id: str`
- `entropy_score: float`