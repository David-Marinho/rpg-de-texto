def turno(personagens: list()):
    continua = True
    prioridade = dict()
    for classe in personagens:
        prioridade[classe] = classe.speed
    personagens = sorted(personagens.key(), reverse=True)

    while continua:
        for personagem in personagens.keys():
            print(f'turno de {personagem}')

            input('digite algo para continuar >>> ')
        

    