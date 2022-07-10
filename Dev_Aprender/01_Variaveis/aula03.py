
#* PROJETO 1 - CADASTRE-ME! 
# todo Modulo 1 - Dados pessoais
""" 
1) Obtenha o nome do usuario
2) Obtenha a idade do usuario
3) Registre automaticamente a data de registro
4) O funcionario recebe de forma aleatorio os valores de bonus:
"""
bonus = ['R$ 50','R$ 100','R$ 200']

#5) Guarde informacoes sobre a data de aniversario (dd/mm/yyyy)

from datetime import datetime
import random
from time import strptime

class User:
    def __init__(self,nome,idade,aniver):
        self.nome = str(nome)
        self.idade = int(idade)
        self.data_registro = datetime.now().date()
        self.aniver = datetime.strptime(aniver,'%d/%m/%Y')
        self.bonus = random.choice(bonus)

    def infos(self):
        print(f''' 
            Ola {self.nome}!
            Seu registro foi concluido com sucesso no dia ({self.data_registro.strftime('%d/%m/%Y')}).
            Parabens, houve um sorteio de bonus e voce ganhou o valor de {self.bonus}!
            ''')


# ---            
nome,idade,nascimento = input('''
                        Insira seu Nome:
                        Idade:
                        Data Nascimento:
                        ''').split(',')

# user_01 = User('Victor',30,'22/07/1991')
user_01 = User(nome,idade,nascimento)
user_01.infos()


# todo Modulo 2 - Mensagem boas vindas



