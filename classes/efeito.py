class efeitos:
    def __init__(self, nome, tempo, status, efeito):
        self.nome = nome
        self.tempo = tempo
        self.status = status
        self.efeito = efeito

    def diminuir_tempo(self):
        self.tempo -= 1
