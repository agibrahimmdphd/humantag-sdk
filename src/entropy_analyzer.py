import random

def analyze_entropy(signal):
    # Simulate entropy as a weighted average of variation in signals
    ppg_var = max(signal["ppg"]) - min(signal["ppg"])
    gsr_var = max(signal["gsr"]) - min(signal["gsr"])
    ekg_var = max(signal["ekg"]) - min(signal["ekg"])
    
    # Normalize and combine
    entropy_score = (ppg_var + gsr_var + ekg_var) / 3
    return entropy_score

