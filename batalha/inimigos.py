from .geral import Geral
from random import randint, choice


class Inimigo(Geral):
    def __init__(self, nome, stats, lv, magia, equip, desc, drop, drop_exp):
        super().__init__(nome, stats, lv, magia, equip)
        self.desc = desc
        self.drops = drop
        self.drop_exp = drop_exp

    def movimendo(self, alvo):
        numero = randint(1, 2)

        if numero == 1:
            self.atacar(alvo)

        elif numero == 2:
            self.defender()
    
    """def enviar_drops(self):
        entrega = list()
        aleatorio = True

        while aleatorio == True:
            drop = randint(1, 100)
            for item in self.drops:
                if item['chance'] == drop:
                    entrega.append(item)
                    item['chance'] -= 5

            aleatorio = choice([True, False])
        
        return entrega"""

        
