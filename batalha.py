def ordem(personagens: dict()):
    return sorted(personagens.key(), reverse=True)

def turno(personagens: list()):
    for classe in personagens:
        prioridade[classe] = classe.speed
    personagens = ordem(prioridade)

    while True:
        

    