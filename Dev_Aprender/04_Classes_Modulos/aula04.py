
#! HERANÇA MULTINIVEL
#evitar vários niveis, cada filho adicionado mais complexidade.

#! HERANÇA MULTIPLA
#irá herdar de duas classes

class Pessoa:
    nome = 'Sou uma pessoa.'
    def convidar():
        print('Ola sou uma pessoa, vamos sair ?')

class Profissional:
    nome = 'Sou um profissional.'
    def convidar():
        print('Ola sou um profissional, vamos sair ?')

class AtorProf (Pessoa,Profissional):
    pass

#Qual classe será considerada para nome ???
# print(AtorProf.nome)

# MRO mostra a ordem das classes > [<class '__main__.AtorProf'>, <class '__main__.Pessoa'>, <class '__main__.Profissional'>, <class 'object'>]
# print(AtorProf.mro())

#*------------
#! MAGIC DUNDER METHODS (__init__) > dunder ou duble underscore;
#são métodos predefinidos em todos os objetos, com invocação automática sob circunstâncias especiais.

""" x,y = 32 ,44
print(x.__add__(y))
w = [3,55,20]
print(w.__len__())
 """
class Pessoa:
    def __init__(self) -> None:
        self.nome = 'Humano'
        self.habilidades = ['hab1','hab2','hab3']

    #repr - mais técnica e em geral usando uma expressão completa que pode ser usada para reconstruir o objeto
    def __repr__(self) -> str:
        return 'Classe com Nome e Habilidades'

    #len - tamanho de algum atributo
    def __len__(self):
        return len(self.habilidades)    
    
    #str - retorna uma string com dados sobre o objeto. Ajuda no Debug.
    def __str__(self) -> str:
        return (f'{self.nome} com as habilidades {self.habilidades} .')

pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))