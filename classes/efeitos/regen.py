from efeito import IEfeito

class Regen(IEfeito):
    def __init__(self, nome, tempo, base):
        self.nome = nome
        self.tempo = tempo
        self.base = base

    def aplicar_efeito(self, alvo):
        if alvo.d_hp < alvo.hp:
            alvo.d_hp += (self.base / 100) * alvo.hp

    def diminuir_tempo(self):
        self.tempo -= 1