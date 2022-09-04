def ordem(personagens):
    return sorted(personagens.key(), reverse=True)

def turno(personagens: list()):
    continua = True
    prioridade = dict()
    for classe in personagens:
        prioridade[classe] = classe.speed
    personagens = ordem(prioridade)

    while continua:
        for personagem in personagens.keys():
            print(f'turno de {personagem}')

            input('digite algo para continuar >>> ')
        

    