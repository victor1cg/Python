#Otavio Miranda - Aula 36 - class method

class Pessoa:
    ano_atual = 2019

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return (self.ano_atual - self.idade)


p1 = Pessoa('luiz',50)
p1.get_ano_nasc()