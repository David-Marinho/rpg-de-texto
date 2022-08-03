class batalha:
    def __init__(self, lista_personagens):
        self.lista_personagens = lista_personagens

    def start(self):
        self.lista_personagens = sorted(self.lista_personagens, key=self.lista_personagens.get)

    def turno(self):
        while True:
            for personagem in self.lista_personagens:
                if personagem == 'pj':
                    escolha = input('escolha sua açao')

                else:
                    """programar inteligencia artificial"""
