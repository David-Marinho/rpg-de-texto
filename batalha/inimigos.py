from .geral import Geral
from random import randint, choice


class Inimigo(Geral):
    def __init__(self, nome, stats, classe, lv, magia, equip, desc, drop, drop_exp):
        super().__init__(nome, stats, lv, magia, equip)
        self.classe = classe
        self.desc = desc
        self.drops = drop
        self.drop_exp = drop_exp

    def movimento(self, alvos):
        if self.classe == 'querreiro':
            personagens = dict()
            selecionados = [{'...': 9999}]

            for alvo in alvos:
                if alvo.stats['hp'] < selecionados[0][1]:
                    selecionados.clear()
                    selecionados.append([alvo, alvo.stats['hp']])
                    
                elif alvo.stats['hp'] == selecionados[0][1]:
                    selecionados.append(alvo, alvo.stats['hp'])
            #comparar a defesa do alvo
            



    
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

        
