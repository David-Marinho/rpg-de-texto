from json import load


class Armas:
    def __init__(self, atk, mag, speed, efeito):
        self.atk = atk
        self.mag = mag
        self.speed = speed
        self.efeito = efeito

    @staticmethod
    def criar_arma(nome, alvo):
        with open(f'dados/equipamentos/armas/{nome}.json', 'r') as dados:
            dados = load(dados)

            atk = dados['atk']
            mag = dados['mag']
            speed = dados['speed']
            efeito = dados['efeito']

        arma = Armas(atk, mag, speed, efeito)
        arma.aplicar_stats(alvo)
        return arma

    def aplicar_stats(self, alvo):
        alvo.total['atk'] = self.atk + alvo.stats['atk']
        alvo.total['mag'] = self.mag + alvo.stats['def']
        alvo.total['speed'] = self.speed + alvo.stats['speed']
