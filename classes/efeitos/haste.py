from efeito import IEfeito

class Haste(IEfeito):
    def __init__(self, tempo):
        self.nome = 'aceleraçao'
        self.tempo = tempo
        self.base = 25

    def aplicar_efeito(self, alvo):
        alvo.d_speed += (self.base/100) * alvo.speed

    def diminuir_tempo(self):
        self.tempo -= 1