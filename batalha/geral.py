from .armas import Armas
from .armadura import Armaduras

class Geral:
    def __init__(self, nome, stats:dict, lv, equip, magias):
        self.nome = nome
        self.stats = stats
        self.total = {
                      'atk': self.stats['atk'], 
                      'def': self.stats['def'], 
                      'mag': self.stats['mag'], 
                      'def_mag': self.stats['def_mag'], 
                      'speed': self.stats['speed']
                      }
        self.lv = lv
        self.defendendo = False
        self.magias = magias
        self.vivo = True
        self.equip = equip
        self.arma = None
        self.armadura = None
        self.lista_efeitos = dict()
        self.total = dict()
        print(self.equip)
        print(self.magias)

    def equipar(self):
        self.arma = Armas.criar_arma(self.equip['arma'], self)
        self.armadura = Armaduras.criar_armadura(self.equip['armadura'], self)
        self.recarregar_stats()

    def atacar(self, alvo_def):
        return self.atk - alvo_def
    
    def defender(self):
        self.defendendo = True

    def verificar_vida(self):
        if self.hp == 0:
            self.vivo = False

    def recarregar_stats(self):
        print(type(self.arma))
        print(type(self.armadura))
        self.arma.aplicar_stats(self)
        self.armadura.aplicar_stats(self)

        self.d_atk = self.total['atk']
        self.d_def = self.total['def']
        self.d_mag = self.total['mag']
        self.d_def_mag = self.total['def_mag']
        self.d_speed = self.total['speed']  

    # funçao que chama outras funçoes no fim do turno
    def finalizar_turno(self):
        self.verificar_vida()
        self.recarregar_Dstats()

        for efeito in self.lista_efeitos:
            efeito.aplicar(self)
