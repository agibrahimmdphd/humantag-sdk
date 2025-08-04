def analyze_entropy(signal):
    return sum(signal['entropy'] for _ in range(1)) > 0.75