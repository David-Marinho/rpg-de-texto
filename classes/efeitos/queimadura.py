from efeito import IEfeito

class Queimadura(IEfeito):
    def __init__(self, tempo):
        self.nome = 'queimadura'
        self.tempo = tempo
        self.base = 10

    def aplicar_efeito(self, alvo):
        alvo.d_hp -= (self.base/100) * alvo.hp

    def diminuir_tempo(self):
        self.tempo -= 1