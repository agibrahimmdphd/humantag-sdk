import numpy as np

class EntropyAnalyzer:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.buffer = []

    def add_sample(self, value):
        self.buffer.append(value)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)

    def compute_entropy_score(self):
        if len(self.buffer) < 2:
            return 0
        diffs = np.diff(self.buffer)
        std_dev = np.std(diffs)
        score = np.clip(std_dev, 0, 1)
        return round(score, 3)