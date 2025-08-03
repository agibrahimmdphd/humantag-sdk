# HumanTag SDK (Prototype)

This SDK simulates biometric signal streaming, entropy analysis, cryptographic signing, and media watermarking verification. It serves as a proof-of-concept for the HumanTag system, designed to verify human presence during media capture.

## Features

- Simulates PPG, EKG, and GSR biometric signals
- Computes real-time entropy scores to evaluate liveness
- Generates mock cryptographic signatures using ECDSA
- Embeds signed payloads into simulated media streams
- Verifies signatures and entropy via public key interface

## Files

- `biometric_stream_simulator.py`: Simulates real-time physiological signals
- `entropy_analyzer.py`: Computes entropy score from signal buffer
- `WatermarkEmbedder.py`: Builds signed payload and simulates watermarking
- `VerificationInterface.py`: Verifies signed payload and entropy score
- `demo_full_pipeline.py`: Runs an end-to-end simulation of the HumanTag system

## Requirements

Install dependencies using:
```bash
pip install ecdsa matplotlib
```

## Run the Demo

```bash
python demo_full_pipeline.py
```

---

This SDK is for demonstration and prototyping only. Do not use in production environments.


---

## License

This project is licensed under the Apache License 2.0.

**Patent Pending**: HumanTag is protected under one or more pending U.S. patent applications. This SDK is provided for demonstration and evaluation purposes only. Unauthorized commercial use is prohibited without written permission.

© 2024 Abdulrahman Ibrahim. All rights reserved.