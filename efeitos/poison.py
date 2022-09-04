from efeito import IEfeito

class Poison(IEfeito):
    def __init__(self, tempo):
        self.nome = 'envenenamento'
        self.tempo = tempo
        self.base = 5

    def aplicar_efeito(self, alvo):
        alvo.d_hp -= (self.base/100) * alvo.hp

    def diminuir_tempo(self):
        self.tempo -= 1