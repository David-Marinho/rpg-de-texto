from personagem import Personagem
from random import randint


class Inimigo(Personagem):
    def __init__(self, nome, hp, atk, defesa, mag, def_mag, speed, lv, lista_magia, desc):
        super().__init__(nome, hp, atk, defesa, mag, def_mag, speed, lv, lista_magia)
        self.desc = desc

    def movimendo(self, alvo):
        numero = randint(1, 2)

        if numero == 1:
            self.atacar(alvo)

        elif numero == 2:
            self.defender()
