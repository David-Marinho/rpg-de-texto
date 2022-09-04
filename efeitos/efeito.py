from abc import ABC, abstractmethod


class IEfeito(ABC):

    @abstractmethod
    def diminuir_tempo(self):
        pass

    @abstractmethod
    def aplicar_efeito(self, alvo):
        pass
