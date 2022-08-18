from random import randint
class Personagem:
    def __init__(self, nome, hp, atk, defesa, mag, def_mag, speed, exp, lv, lista_magia, lista_inventario):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.mag = mag
        self.def_mag = def_mag
        self.speed = speed
        self.exp = exp
        self.lv = lv
        self.defendendo = False
        self.lista_magia = lista_magia
        self.lista_inventario = lista_inventario

    def atacar(self, inimigo_def):
        return self.atk - inimigo_def

    def defender(self):
        self.defendendo = True

    def fugir(self):
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

    def finalizar_turno(self):
        #fazer isso
        pass




