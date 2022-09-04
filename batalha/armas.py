from json import load


class Armas:
    def __init__(self):
        self.atk = None
        self.mag = None
        self.speed = None
        self.efeito = None

    def criar_arma(self, nome):
        with open(f'../dados/equipamentos/armas/{nome}', 'r') as dados:
            dados = load(dados)

            self.atk = dados['atk']
            self.mag = dados['mag']
            self.speed = dados['speed']
            self.efeito = dados['efeito']
