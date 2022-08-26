from personagem import Personagem
from random import randint, choice


class Inimigo(Personagem):
    def __init__(self, nome, hp, atk, defesa, mag, def_mag, speed, lv, magias, desc, drop, drop_exp):
        super().__init__(nome, hp, atk, defesa, mag, def_mag, speed, lv, magias)
        self.desc = desc
        self.drops = drop
        self.drop_exp = drop_exp

    def movimendo(self, alvo):
        numero = randint(1, 2)

        if numero == 1:
            self.atacar(alvo)

        elif numero == 2:
            self.defender()
    
    def enviar_drops(self):
        entrega = list()
        aleatorio = True

        while aleatorio == True:
            drop = randint(1, 100)
            for item in self.drops:
                if item['chance'] == drop:
                    entrega.append(item)
                    item['chance'] -= 5

            aleatorio = choice([True, False])
        
        return entrega

        
