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

    def equipamentos(self):
        self.arma = Armas()
        self.armadura = Armaduras()
        self.aplicar_equip()
    
    def aplicar_equip(self):
        self.atk += self.arma.atk
        self.mag += self.arma.mag
        self.speed += self.arma.speed

        self.hp += self.armadura.hp
        self.defesa += self.armadura.defesa
        self.def_mag += self.armadura.def_mag
        self.speed += self.armadura.speed

        self.recarregar_d_stats()

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



    def level_up(self):
        if self.exp >= 100:
            self.atk += 2
            self.defesa += 2
            self.mag += 2
            self.def_mag += 2
            self.speed += 2
            self.hp += 10
