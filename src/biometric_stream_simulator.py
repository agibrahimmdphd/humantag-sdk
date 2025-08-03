import numpy as np

class BiometricStreamSimulator:
    def __init__(self, signal_type='PPG', noise_level=0.05):
        self.signal_type = signal_type.upper()
        self.noise_level = noise_level
        self.t = 0
        self.dt = 0.1

    def _ppg_waveform(self, t):
        return 1.0 + 0.6 * np.sin(2 * np.pi * 1.2 * t) + 0.2 * np.sin(2 * np.pi * 2.4 * t)

    def _ekg_waveform(self, t):
        return 1.2 * np.sin(2 * np.pi * 1.0 * t) + 0.5 * np.sin(4 * np.pi * t)

    def _gsr_waveform(self, t):
        return 0.5 + 0.05 * np.sin(2 * np.pi * 0.2 * t) + 0.02 * np.random.randn()

    def get_sample(self):
        self.t += self.dt
        if self.signal_type == 'PPG':
            signal = self._ppg_waveform(self.t)
        elif self.signal_type == 'EKG':
            signal = self._ekg_waveform(self.t)
        elif self.signal_type == 'GSR':
            signal = self._gsr_waveform(self.t)
        else:
            raise ValueError(f"Unsupported signal type: {self.signal_type}")
        return signal + self.noise_level * np.random.randn()

    def stream(self, duration=10):
        timestamps = []
        values = []
        while self.t < duration:
            value = self.get_sample()
            timestamps.append(self.t)
            values.append(value)
        return timestamps, values