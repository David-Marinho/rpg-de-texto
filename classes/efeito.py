from json import load


class Efeito:
    def __init__(self, nome, tempo, status, calculo, valor):
        self.nome = nome
        self.tempo = tempo
        self.status = status
        self.calculo = calculo
        self.valor = valor

    @staticmethod
    def criar_efeito(nome):
        with open(f'../dados/efeitos/{nome}') as dados:
            dados = load(dados)

            efeito = Efeito(dados['nome'], dados['tempo'], dados['status'], dados['calculo'], dados['valor'])

        return efeito

    def aplicar_efeito(self, alvo):
        if self.status == 'hp':
            if self.calculo == "porcentagem":
                alvo.hp += (self.valor / 100) * alvo.hp

            else:
                alvo.hp += self.valor

        self.diminuir_tempo()

    def diminuir_tempo(self):
        self.tempo -= 1
