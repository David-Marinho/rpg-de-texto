from personagem import Personagem
from random import randint
from armas import Armas
from armadura import Armaduras


class Jogador(Personagem):
    def __init__(self, nome, hp, atk, mana, defesa, mag, def_mag, speed, exp, lv, magias, inventario, equip):
        super().__init__(nome, hp, atk, mana, defesa, mag, def_mag, speed, lv, magias)
        self.exp = exp
        self.inventario = inventario
        self.equip = equip
        self.arma = None
        self.armadura = None
        self.Datk = 0
        self.Ddef = 0
        self.Dmag = 0
        self.Ddef_mag = 0
        self.Dspeed = 0

    def equipamentos(self):
        arma = Armas()
        armadura = Armaduras()
        self.recarregar_Dstats(arma, armadura)

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

    def recarregar_Dstats(self, arma, armadura):
        self.Datk = self.atk + arma.atk
        self.Ddef = self.defesa + armadura.defesa
        self.Dmag = self.mag + arma.mag
        self.Ddef_mag = self.def_mag + armadura.def_mag
        self.Dspeed = self.speed + arma.speed + armadura.speed

    def level_up(self):
        if self.exp >= 100:
            self.atk += 2
            self.defesa += 2
            self.mag += 2
            self.def_mag += 2
            self.speed += 2
            self.hp += 10
