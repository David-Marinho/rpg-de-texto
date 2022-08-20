from personagem import Personagem
from random import randint


class Jogador(Personagem):
    def __init__(self, nome, hp, atk, defesa, mag, def_mag, speed, exp, lv, lista_magia, lista_inventario):
        super().__init__(nome, hp, atk, defesa, mag, def_mag, speed, lv, lista_magia)
        self.exp = exp
        self.lista_inventario = lista_inventario

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
