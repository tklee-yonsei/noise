from abc import ABC, abstractmethod

class NoiseAdder(ABC):
    @abstractmethod
    def add_noise(self, symbols, snr_db):
        pass

    @abstractmethod
    def process_request(self, symbols_real_imag, snr_db):
        pass
