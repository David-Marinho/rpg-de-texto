from json import load


class Armaduras:
    def __init__(self):
        self.defesa = None
        self.def_mag = None
        self.speed = None

    def criar_armadura(self, nome):
        with open(f'../dados/equipamentos/armaduras/{nome}', 'r') as dados:
            dados = load(dados)

            self.defesa = dados['defesa']
            self.def_mag = dados['def_mag']
            self.speed = dados['speed']
