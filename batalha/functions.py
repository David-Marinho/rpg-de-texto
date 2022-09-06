def turno(lista):
    continua = True
    prioridade = dict()
    for classe in lista:
        prioridade[classe] = classe.stats['speed']

    while continua:
        for personagem in sorted(prioridade, key=prioridade.get, reverse=True):
            print(f'turno de {personagem.nome}')

            input('digite algo para continuar >>> ')
        

    