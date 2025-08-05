# HumanTag Entropy Threshold Benchmarking Plan

## Objective
To empirically determine an optimal entropy threshold to distinguish between real human biometric signals and synthetic/spoofed data for use in HumanTag's biometric verification pipeline.

## Signal Types
- Photoplethysmography (PPG)
- Galvanic Skin Response (GSR)
- Electrocardiogram (EKG)
- Electromyogram (EMG)
- Optional: EEG, respiration rate, temperature

## Sample Size
- 50–100 real human participants (live capture)
- 50–100 simulated spoof/fake sessions
- Optional: Include AI-generated biometric streams

## Data Acquisition
- Collect real-time biometric signal streams using FDA-cleared or research-grade wearable sensors
- Spoof/fake data collected using:
  - Playback recordings
  - Static synthetic data
  - AI-generated biometric streams

## Entropy Metrics
- Shannon Entropy
- Sample Entropy (SampEn)
- Approximate Entropy (ApEn)
- Variance-based proxy (used in SDK for demonstration)

## Statistical Analysis
- Histogram overlays of real vs. fake distributions
- Receiver Operating Characteristic (ROC) analysis
- Area Under the Curve (AUC) metrics
- Determine true positive rate (TPR) vs. false positive rate (FPR) for different thresholds

## Deliverables
- Recommended entropy threshold value(s)
- Sensitivity-specificity tradeoff charts
- Justification for threshold choice (e.g. ≥0.3)
- White paper or appendix for regulatory or enterprise customers

## Timeline Estimate
- Data collection: 2–4 weeks
- Analysis and modeling: 2 weeks
- Final validation and reporting: 1 week

## Notes
This plan supports evidence-based tuning of the entropy threshold in HumanTag and enhances defensibility under HIPAA, FDA, or GDPR-aligned frameworks.