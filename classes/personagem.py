class Personagem:
    def __init__(self, hp, atk, defesa, mag, def_mag, speed, possui_efeito):
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.mag = mag
        self.def_mag = def_mag
        self.speed = speed
        self.possui_efeito = possui_efeito
        self.efeitos = list()
