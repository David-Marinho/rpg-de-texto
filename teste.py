import json
from json import load
from jogador import Jogador
from inimigos import Inimigo

dados = load(open('dados/jogador/jogador.json', 'r'))
inimigo = load(open('dados/monstros/generico.json', 'r'))

pessoa = Jogador(dados['nome'], dados['hp'], dados['atk'], dados['mana'], dados['def'], dados['mag'], dados['def_mag'],
                 dados['speed'], dados['exp'], dados['lv'], dados['magia'], dados['inventario'], dados['equip'])


"""inimigo = Inimigo(inimigo['nome'], inimigo['hp'], inimigo['atk'], inimigo['def'], inimigo['mag'], inimigo['def_mag'],
                  inimigo['speed'], inimigo['lv'], inimigo['magia'], inimigo['desc'])

testes = open('dados/jogador/teste.json', 'w')

json.dump(pessoa, testes)"""

print(pessoa.Datk)
