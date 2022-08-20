class Personagem:
    def __init__(self, nome, hp, atk, defesa, mag, def_mag, speed, lv, lista_magia):
        self.nome = nome
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.mag = mag
        self.def_mag = def_mag
        self.speed = speed
        self.lv = lv
        self.defendendo = False
        self.lista_magia = lista_magia
        self.vivo = True

    def verificar_vida(self):
        if self.hp == 0:
            self.vivo = False

    def atacar(self, inimigo_def):
        return self.atk - inimigo_def

    def defender(self):
        self.defendendo = True

    # funçao que chama outras funçoes no fim do turno
    def finalizar_turno(self):
        self.verificar_vida()
