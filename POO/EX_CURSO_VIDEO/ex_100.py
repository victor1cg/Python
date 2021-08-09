 # ------ Ex 100) Faça um programa que tenha uma lista chamada numeros
 #e duas funções chamadas sorteio() e somaPar()
 #A sorteio vai sortear 5 numeros e vai coloca-los dentro da lista
 #a somaPar vai mostrar a soma de todos os numeros pares'''
from random import randint 

def sorteia (lista):
    for cont in range (0,5):
        lista.append(randint(1, 100))

numeros = list()
sorteia(numeros)
print(numeros)

def somaPar(lista):
    