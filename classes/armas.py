import os
from efeito import efeitos
from json import load


class armas:
    def __init__(self, hp, atk, mag, defesa, speed):
        self.hp = hp
        self.atk = atk
        self.mag = mag
        self.defesa = defesa
        self.speed = speed
        self.efeito = None

    def definir_efeito(self, nome_efeito):
        path = rf'{os.getcwd()}\dados\efeitos'
        for file in os.listdir(path):
            print()
            if file == f'{nome_efeito}.json':
                arq = load(open(rf'{path}\{file}', 'r'))
                self.efeito = efeitos(arq['nome'], arq['tempo'], arq['status'], arq['efeito'])
                break

            else:
                pass
