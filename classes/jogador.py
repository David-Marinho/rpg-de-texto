from personagem import Personagem
from random import randint


class Jogador(Personagem):
    def __init__(self, nome, hp, atk, mana, defesa, mag, def_mag, speed, exp, lv, magias, inventario, Datk, Ddef, Dmag, Ddef_mag, Dspeed):
        super().__init__(nome, hp, atk, mana, defesa, mag, def_mag, speed, lv, lista_magia)
        self.exp = exp
        self.inventario = inventario
        self.Datk = Datk
        self.Ddef = Ddef
        self.Dmag = Dmag
        self.Ddef_mag = Ddef_mag
        self.Dspeed = Dspeed

    @staticmethod
    def fugir():
        chance = randint(1, 100)

        if chance <= 20:
            print('fugiu')

        else:
            print('nao conseguiu fugir')

    def inventario(self):
        numero = 1
        for item in self.lista_inventario:
            print(f'{numero} -> {item["nome"]} ------ {item["quant"]}')

        escolha = int(input('digite um numero: '))
        # chamar o efeito do item
        self.lista_inventario[escolha]['quant'] -= 1
    
    def recarregar_Dstats(self):
        self.Datk = self.atk + arma.atk + armadura.atk
        self.Ddef = self.defesa + arma.defesa + armadura.defesa
        self.Dmag = self.mag + arma.mag + armadura.mag
        self.Ddef_mag = self.def_mag + arma.def_mag + armadura.def_mag
        self.Dspeed = self.speed + arma.speed + armadura.speed
    
    def level_up(self):
        if self.exp >= 100:
            self.atk += 2
            self.defesa += 2
            self.mag += 2
            self.def_mag += 2
            self.speed += 2
            self.hp += 10
