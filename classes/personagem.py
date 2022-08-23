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
        self.defendendo = False
        self.magias = magias
        self.vivo = True

    def verificar_vida(self):
        if self.hp == 0:
            self.vivo = False

    @staticmethod
    def atacar(atk, inimigo_def):
        return atk - inimigo_def

    def defender(self):
        self.defendendo = True

    # funçao que chama outras funçoes no fim do turno
    def finalizar_turno(self):
        self.verificar_vida()
