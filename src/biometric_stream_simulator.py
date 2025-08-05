import random

def generate_biometric_stream():
    return {
        "ppg": [random.uniform(0.8, 1.2) for _ in range(10)],
        "gsr": [random.uniform(0.1, 0.5) for _ in range(10)],
        "ekg": [random.uniform(0.7, 1.3) for _ in range(10)]
    }

