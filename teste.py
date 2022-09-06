from json import load
from batalha import Jogador
from batalha import Inimigo
from batalha import functions

def carrega_jogador():
    dados = load(open('dados/jogador/jogador.json', 'r'))

    return Jogador(dados['nome'], dados['stats'],dados['lv'], dados['equip'] , dados['exp'], dados['inventario'], dados['magia'])

def carrega_inimigo():
    inimigo = load(open('dados/monstros/generico.json', 'r'))

    return Inimigo(inimigo['nome'], inimigo['stats'], inimigo['lv'],inimigo['equip'], inimigo['magia'], inimigo['desc'], inimigo['drops'], inimigo['drop exp'])

pessoa = carrega_jogador()
inimigo = carrega_inimigo()

functions.turno([pessoa, inimigo])

