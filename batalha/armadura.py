from json import load


class Armaduras:
    def __init__(self):
        self.defesa = None
        self.def_mag = None
        self.speed = None

    def criar_armadura(self, nome, alvo):
        with open(f'../dados/equipamentos/armaduras/{nome}', 'r') as dados:
            dados = load(dados)

            self.hp = dados['hp']
            self.defesa = dados['defesa']
            self.def_mag = dados['def_mag']
            self.speed = dados['speed']
            self.aplicar_stats(alvo)

    def aplicar_stats(self, alvo):
        alvo.total['hp'] = self.hp + alvo.stats['hp']
        alvo.total['def'] = self.defesa + alvo.stats['def']
        alvo.total['def_mag'] = self.def_mag + alvo.stats['def_mag']
        alvo.total['speed'] = self.speed + alvo.stats['speed']
