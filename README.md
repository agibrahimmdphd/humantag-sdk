# HumanTag SDK v1.3
This SDK provides biometric watermarking + verification...
## Licensing & Patent Status

This project is released under the **Apache License 2.0**.

You are free to:
- Use, modify, and distribute this SDK in commercial or research applications
- Integrate into third-party platforms under the terms of the Apache License

**Patent Pending:**  
The HumanTag™ biometric watermarking and real-time verification system is patent pending in the United States and is covered by one or more unpublished applications.

### Licensing Highlights:
- Open-source for research and enterprise integration
- Explicit patent grant under Apache 2.0 terms
- Includes replay protection, entropy validation, and cryptographic signature verification
- Designed to be trustable in high-risk AI media environments (e.g., law enforcement, journalism, healthcare, defense)

See the full `LICENSE` file and `NOTICE.txt` for legal terms.

## 📊 Entropy Analysis Tools

This SDK includes scientific tooling to evaluate signal entropy:

- `tools/entropy_distribution_simulator.py` – plot real vs. fake entropy
- `tools/entropy_distribution_simulation.png` – saved plot
- `tools/entropy_benchmark_plan.md` – research plan for validating threshold

Use this for clinical calibration, regulatory support, or investor demos.

## 🧪 Real-Time Verification Logic

The `VerificationInterface.py` module now includes:
- Entropy gating (default threshold: `0.3`)
- Spoof detection warnings
- Configurable parameters

✅ Output: `✅ Verified = True` or spoof alert

