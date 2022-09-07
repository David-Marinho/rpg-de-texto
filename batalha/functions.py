from .jogador import Jogador

def turno(lista):
    continua = True
    lista_inimigos = list()
    lista_jogadores = list()

    prioridade = dict()
    for classe in lista:
        prioridade[classe] = classe.stats['speed']

    while continua:
        for personagem in sorted(prioridade, key=prioridade.get, reverse=True):
            print(f'turno de {personagem.nome}')
            personagem.iniciar_turno()

            if type(personagem) is Jogador:
                move = int(input('[1]atacar \n [2]defender \n [3] fugir \n [4]verificar stats \n >>>'))

                if move == 1:
                    for char in prioridade.keys():
                        if type(char) is not Jogador:
                            lista_inimigos.append(char)

                    num = 1
                    for ini in lista_inimigos:
                        print(f'[{num}] - {ini.nome}')
                    
                    alvo = int(input('digite o numero do alvo >>>'))
                    personagem.atacar(lista_inimigos[alvo - 1])
            
                elif move == 2:
                    personagem.defender()
                
                elif move == 4:
                    personagem.verificar_stats()

            else:
                for char in prioridade.keys():
                    if type(char) is Jogador:
                        lista_jogadores.append(char)

                personagem.movimento(lista_jogadores)
            
            lista_inimigos.clear()
            lista_jogadores.clear()
        

    