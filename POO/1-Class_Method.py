#Otavio Miranda - Aula 36 - class method
from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self,nome,idade):      #__init__ construtor
        self.nome = nome                
        self.idade = idade

    def get_ano_nasc(self):             #metodo de instancias, usa SELF
        return print('\n',\
            self.ano_atual - self.idade)

    @classmethod                        #não precisa da instancia, mas da CLASSE
    def por_ano_nasc(cls,nome,ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome,idade)

    @staticmethod                       #Métodos estáticos não precisam de uma referência, não recebem um primeiro argumento especial (self). 
    def gera_id():                      #É como uma função simples que, por acaso, reside no corpo de uma classe em vez de ser definida no nível do módulo.    
        rand = randint(10000,19999)

        
p1 = Pessoa('luiz',50)                  
p1.get_ano_nasc()

'''
pessoa = Pessoa (). Instancia é um elemento da classe. 
Elemento que pertence a classe Pessoa, contendo todos os ATRIBUTOS e METODOS.
pessoa.nome , pessoa.idade, etc
pessoa é uma instancia da classe Pessoa. OU Objeto de Pessoa.
'''
#Atributos de Classe 
class A:
    vc= 123

    def __init__(self):
        self.vc = 321

print(A.vc)
A.vc= 'alterado'
a1 = A()
print(A.vc)