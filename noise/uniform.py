import numpy as np

from noise.interface import NoiseAdder


class UniformNoiseAdder(NoiseAdder):
    def add_noise(self, symbols, snr_db):
        snr_linear = 10 ** (snr_db / 10)
        signal_power = np.mean(np.abs(symbols)**2)
        noise_power = signal_power / snr_linear
        noise = np.sqrt(12 * noise_power) * (np.random.rand(len(symbols)) - 0.5)
        noisy_symbols = symbols + noise
        return noisy_symbols

    def process_request(self, symbols_real_imag, snr_db):
        try:
            symbols = np.array([complex(s[0], s[1]) for s in symbols_real_imag])
        except (TypeError, IndexError, ValueError):
            raise ValueError('Invalid symbols data format')
        noisy_symbols = self.add_noise(symbols, snr_db)
        noisy_symbols_real_imag = [[s.real, s.imag] for s in noisy_symbols]
        return noisy_symbols_real_imag
