from json import load


class Armas:
    def __init__(self):
        self.atk = None
        self.mag = None
        self.speed = None
        self.efeito = None

    def criar_arma(self, nome, alvo):
        with open(f'../dados/equipamentos/armas/{nome}', 'r') as dados:
            dados = load(dados)

            self.atk = dados['atk']
            self.mag = dados['mag']
            self.speed = dados['speed']
            self.efeito = dados['efeito']
            self.aplicar_stats(alvo)

    def aplicar_stats(self, alvo):
        alvo.total['atk'] = self.atk + alvo.stats['atk']
        alvo.total['mag'] = self.mag + alvo.stats['def']
        alvo.total['speed'] = self.speed + alvo.stats['speed']
