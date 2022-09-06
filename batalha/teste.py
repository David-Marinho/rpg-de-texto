class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class aluno(pessoa):
    def __init__(self, curso, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso


aluno1 = aluno('cco', 'joao', 20)

print(aluno1.nome)