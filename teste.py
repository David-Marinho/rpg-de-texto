from json import load
from batalha import Jogador
from batalha import Inimigo
from batalha import functions

def carrega_jogador():
    dados = load(open('dados/jogador/jogador.json', 'r'))

    return Jogador(dados['nome'], dados['stats'],dados['lv'], dados['equip'] , dados['exp'], dados['inventario'], dados['magia'])

def carrega_inimigo():
    inimigo = load(open('dados/monstros/generico.json', 'r'))

    return Inimigo(inimigo['nome'], inimigo['stats'], inimigo['classe'], inimigo['lv'],inimigo['equip'], inimigo['magia'], inimigo['desc'], inimigo['drops'], inimigo['drop exp'])

pessoa = carrega_jogador()
inimigo = carrega_inimigo()

print(pessoa)
print(type(pessoa))
print(type(inimigo))

if type(pessoa) is Jogador:
    print('é um jogador')

functions.turno([pessoa, inimigo])

