
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