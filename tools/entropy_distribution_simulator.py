import matplotlib.pyplot as plt
import numpy as np

# Simulated entropy values for real and fake signals
np.random.seed(42)
real_entropy = np.random.normal(loc=0.45, scale=0.05, size=100)
fake_entropy = np.random.normal(loc=0.20, scale=0.04, size=100)

# Clip entropy to [0, 1]
real_entropy = np.clip(real_entropy, 0, 1)
fake_entropy = np.clip(fake_entropy, 0, 1)

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(real_entropy, bins=20, alpha=0.7, label='Real (Live)', color='green')
plt.hist(fake_entropy, bins=20, alpha=0.7, label='Fake (Spoofed)', color='red')
plt.axvline(x=0.3, color='blue', linestyle='--', linewidth=2, label='Threshold (0.3)')
plt.xlabel("Entropy Score")
plt.ylabel("Frequency")
plt.title("Simulated Entropy Distribution: Real vs. Fake Biometric Signals")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("entropy_distribution_simulation.png")
plt.show()