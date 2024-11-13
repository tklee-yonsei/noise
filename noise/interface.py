from abc import ABC, abstractmethod

class NoiseAdder(ABC):
    """ 
    NoiseAdder 클래스는 노이즈 추가 기능을 위한 추상 기본 클래스입니다.
    
    이 클래스는 노이즈를 추가하는 방법을 정의하는 두 개의 추상 메서드를 포함하고 있습니다.
    이 클래스를 상속받는 모든 클래스는 이 메서드들을 구현해야 합니다.
    """

    @abstractmethod
    def add_noise(self, symbols, snr_db):
        """ 
        주어진 심볼에 노이즈를 추가합니다.

        Parameters
        ----------
        symbols : array-like
            노이즈를 추가할 심볼의 배열입니다.
        snr_db : float
            신호 대 노이즈 비율(SNR)을 데시벨 단위로 나타낸 값입니다.

        Returns
        -------
        array-like
            노이즈가 추가된 심볼의 배열입니다.
        """
        pass

    @abstractmethod
    def process_request(self, symbols_real_imag, snr_db):
        """ 
        실수 및 허수 쌍으로 표현된 심볼을 처리하여 노이즈가 추가된 심볼을 반환합니다.

        Parameters
        ----------
        symbols_real_imag : list of lists
            실수 및 허수 쌍으로 구성된 심볼의 리스트입니다.
        snr_db : float
            신호 대 노이즈 비율(SNR)을 데시벨 단위로 나타낸 값입니다.

        Returns
        -------
        list of lists
            노이즈가 추가된 심볼의 실수 및 허수 쌍 리스트입니다.
        """
        pass
