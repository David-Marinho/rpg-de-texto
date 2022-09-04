from .geral import Geral
from random import randint
from .armas import Armas
from .armadura import Armaduras


class Jogador(Geral):
    def __init__(self, stats, total, lv, magias, exp, inventario, equip):
        super().__init__(stats, total, lv, magias)
        self.exp = exp
        self.inventario = inventario
        self.equip = equip
        self.arma = None
        self.armadura = None
        

        self.equipar()

    def equipar(self):
        self.arma = Armas(self.equip['arma'])
        self.armadura = Armaduras(self.equip['armadura'])

        self.total['atk'] += self.arma.atk
        self.total['mag'] += self.arma.mag
        self.total['spd'] += self.arma.speed

        self.total['hp'] += self.armadura.hp
        self.total['def'] += self.armadura.defesa
        self.total['def_mag'] += self.armadura.def_mag
        self.total['spd'] += self.armadura.speed

        self.recarregar_d_stats(self.total)

    @staticmethod
    def fugir():
        chance = randint(1, 100)

        if chance <= 20:
            print('fugiu')

        else:
            print('nao conseguiu fugir')

    def ver_inventario(self):
        numero = 1
        for item in self.inventario:
            print(f'{numero} -> {item["nome"]} ------ {item["quant"]}')

        escolha = int(input('digite um numero: '))
        # chamar o efeito do item
        self.inventario[escolha]['quant'] -= 1



    def check_exp(self):
        if self.exp >= 100:
            self.stats['atk'] += 2
            self.stats['defesa'] += 2
            self.stats['mag'] += 2
            self.stats['def_mag'] += 2
            self.stats['speed'] += 2
            self.stats['hp'] += 10
