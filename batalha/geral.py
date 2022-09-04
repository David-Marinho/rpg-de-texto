class Geral:
    def __init__(self, nome, stats:dict, lv, magias):
        self.nome = nome
        self.stats = stats
        self.total = {
                      'atk': self.stats['atk'], 
                      'def': self.stats['def'], 
                      'mag': self.stats['mag'], 
                      'def_mag': self.stats['def_mag'], 
                      'speed': self.stats['speed']
                      }
        self.defendendo = False
        self.magias = magias
        self.vivo = True
        self.lista_efeitos = []


    def atacar(self, alvo_def):
        return self.atk - alvo_def
    
    def defender(self):
        self.defendendo = True

    def verificar_vida(self):
        if self.hp == 0:
            self.vivo = False

    def recarregar_d_stats(self, base):
        self.d_atk = base['atk']
        self.d_def = base['def']
        self.d_mag = base['mag']
        self.d_def_mag = base['def_mag']
        self.d_speed = base['speed']  

    # funçao que chama outras funçoes no fim do turno
    def finalizar_turno(self):
        self.verificar_vida()
        self.recarregar_Dstats()

        for efeito in self.lista_efeitos:
            efeito.aplicar(self)
