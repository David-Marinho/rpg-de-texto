import json

lugar = json.load(open('dados/lugares/capital/principal.json', 'r'))

coisa = json.load(open(f'{lugar["telas"]["praca central"]}', 'r'))

cont = 0
for i in lugar['telas']:
    cont += 1
    print(f'[{cont}] - {i}')

escolha = int(input('digite um numero: '))

lista = list(lugar['telas'].keys())
print(lista[escolha - 1])