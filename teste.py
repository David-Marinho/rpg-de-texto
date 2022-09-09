from json import load
from batalha import Jogador
from batalha import Inimigo
from batalha import functions

def carrega_jogador(local):
    dados = load(open(f'dados/jogador/{local}.json', 'r'))

    return Jogador(dados['nome'], dados['stats'],dados['lv'], dados['equip'] , dados['exp'], dados['inventario'], dados['magia'])

def carrega_inimigo():
    inimigo = load(open('dados/monstros/generico.json', 'r'))

    return Inimigo(inimigo['nome'], inimigo['stats'], inimigo['classe'], inimigo['lv'],inimigo['equip'], inimigo['magia'], inimigo['desc'], inimigo['drops'], inimigo['drop exp'])

pessoa = carrega_jogador('jogador')
pessoa2 = carrega_jogador('jogador 2')
inimigo = carrega_inimigo()

alvos = [pessoa, pessoa2]
selecionados = [['...', 9999]]



"""print(pessoa)
print(type(pessoa))
print(type(inimigo))

if type(pessoa) is Jogador:
    print('é um jogador')

functions.turno([pessoa, inimigo])"""

