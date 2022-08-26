class Personagem:
    def __init__(self, nome, hp, atk, mana, defesa, mag, def_mag, speed, lv, magias):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.mana = mana
        self.defesa = defesa
        self.mag = mag
        self.def_mag = def_mag
        self.speed = speed
        self.lv = lv
        self.d_hp = hp
        self.d_atk = atk
        self.d_mana = mana
        self.d_def = defesa
        self.d_mag = mag
        self.d_def_mag = def_mag
        self.d_speed = speed
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

    def recarregar_d_stats(self):
        self.d_atk = self.atk
        self.d_def = self.defesa
        self.d_mag = self.mag
        self.d_def_mag = self.def_mag
        self.d_speed = self.speed

        for efeito in self.lista_efeitos:
            efeito.aplicar(self)

    # funçao que chama outras funçoes no fim do turno
    def finalizar_turno(self):
        self.verificar_vida()
        self.recarregar_Dstats()
