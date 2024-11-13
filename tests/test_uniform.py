import unittest
import numpy as np
from noise.uniform import UniformNoiseAdder  # UniformNoiseAdder 클래스 임포트


class TestUniformNoiseAdder(unittest.TestCase):
    """UniformNoiseAdder 클래스의 유닛 테스트를 위한 클래스입니다."""

    def setUp(self):
        """각 테스트 전에 실행되는 설정 메서드입니다."""
        self.adder = UniformNoiseAdder()

    def test_add_noise(self):
        """add_noise 메서드의 동작을 테스트합니다."""
        symbols = np.array([1 + 1j, 2 + 2j, 3 + 3j])
        snr_db = 10
        noisy_symbols = self.adder.add_noise(symbols, snr_db)

        # 노이즈가 추가된 심볼의 크기를 확인합니다.
        self.assertEqual(len(noisy_symbols), len(symbols))
        self.assertFalse(
            np.array_equal(noisy_symbols, symbols), "노이즈가 추가되지 않았습니다."
        )

    def test_process_request(self):
        """process_request 메서드의 동작을 테스트합니다."""
        symbols_real_imag = [[1, 1], [2, 2], [3, 3]]
        snr_db = 10
        noisy_symbols = self.adder.process_request(symbols_real_imag, snr_db)

        # 노이즈가 추가된 심볼의 크기를 확인합니다.
        self.assertEqual(len(noisy_symbols), len(symbols_real_imag))
        self.assertFalse(
            np.array_equal(noisy_symbols, symbols_real_imag),
            "노이즈가 추가되지 않았습니다.",
        )


if __name__ == "__main__":
    unittest.main()
