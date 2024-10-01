
#! DECORATOR - Aproveitando funções prontas
""" 
def deposito_dinheiro():
    print('Depositando dinhero')
    def deposito_usd():
        print('Depositando USD')
    def deposito_brl():
        print('Depositando BRL')
    deposito_usd()
    deposito_brl()

deposito_dinheiro() 

#Guardar uma função
def pai(numero):
    def filho1():
        print('filho 1')
    def filho2():
        print('filho 2')
    if numero == 1:
        return filho1

resultado = pai(1)          #numero = 1 
resultado()                 #resultado contem a função filho1
"""
#Garantir o fluxo das funções

def meu_decorator(f):
    def wrapper():
        print('Antes')
        f()                     #utilizo o argumento como função
        print('Depois')
    return wrapper              #retorno da propria função - REFERENCIA


def parabens():
    print('Parabens')

# Essa parte logica é possivel substituir por @meu_decorator, acima de parabens
resultado = meu_decorator(parabens) #*@meu_decorator
resultado()

######## ----------- Parte 3 DECORATOR

#! sem utilizar decorator
#decorador é uma forma de mudar o output de uma funçao
#assim que funciona o decorador no backend
'''def soma(x,y):
    return x+y

def validar(f,x,y):
    def valida():
        if x < 0 or y < 0:
            raise ValueError('X e Y precisam ser positivos\n')
        return f(x,y)
    return valida

# x = validar(soma, 10,-5)()
'''
#! Utilizando decorator

def validar2(f):                        #validar2 recebe a f = soma2
    def valida2(x,y):                   #
        if x < 0 or y < 0:
            raise ValueError('X e Y precisam ser positivos\n')
        return f(x,y)                   #retorna f >> soma \ x e y como variaveis
    return valida2

@validar2
def soma2(x,y):                         #soma 2 será uma funcao dentro de validar2
    return x + y

a = soma2(10,12)
print(a)
