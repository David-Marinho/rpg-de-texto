from json import load
from jogador import Jogador
from inimigos import Inimigo

jogador = load(open('dados/jogador/jogador.json', 'r'))
inimigo = load(open('dados/monstros/generico.json', 'r'))

jogador = Jogador(jogador['nome'], jogador['hp'], jogador['atk'], jogador['def'], jogador['mag'], jogador['def_mag'],
                  jogador['speed'], jogador['exp'], jogador['lv'], jogador['magia'], jogador['inventario'])

inimigo = Inimigo(inimigo['nome'], inimigo['hp'], inimigo['atk'], inimigo['def'], inimigo['mag'], inimigo['def_mag'],
                  inimigo['speed'], inimigo['lv'], inimigo['magia'], inimigo['desc'])






