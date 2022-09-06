from json import load


class Armaduras:
    def __init__(self, hp, defesa, def_mag, speed, efeito):
        self.hp = hp
        self.defesa = defesa
        self.def_mag = def_mag
        self.speed = speed
        self.efeito = efeito

    @staticmethod
    def criar_armadura(nome, alvo):
        with open(f'dados/equipamentos/armaduras/{nome}.json', 'r') as dados:
            dados = load(dados)

            hp = dados['hp']
            defesa = dados['defesa']
            def_mag = dados['def_mag']
            speed = dados['speed']
            efeito = dados['efeito']
            
        armadura = Armaduras(hp, defesa, def_mag, speed, efeito)
        return armadura

    def aplicar_stats(self, alvo):
        alvo.total['hp'] = self.hp + alvo.stats['hp']
        alvo.total['def'] = self.defesa + alvo.stats['def']
        alvo.total['def_mag'] = self.def_mag + alvo.stats['def_mag']
        alvo.total['speed'] = self.speed + alvo.stats['speed']
