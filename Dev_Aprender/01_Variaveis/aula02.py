
#! SPLIT e JOIN

frase = 'Ola! bem vindo, a esse treinamento'

print(frase.split())
print(frase.split(','))

nomes = 'jow,rafael, carol, amanda,jeff'
print(nomes.split(',',3))       # qtd de ocorrencias a PARAR de separar
print(nomes.split())            #Padrão é separar espaços

hasht = '#music #play #guitar #python'
print(hasht.split('#'))
hasht_separados = hasht.split('#')

print(','.join(hasht_separados)) #Metodo para realizar join de strings com a virgula


# ! INPUT
senha = input('quantos filmes voce ja viu esse mes ? \n')
print(type(senha))
senha = int(senha)
print(type(senha))


# ! Tipos de Numeros utilizados

a = 20
b = 20.5

print(type(a),type(b))

print(10 // 6)  #divisao de inteiro
print(10 % 6)   #resto da divisao
print(10 ** 6)  #exponencial

a += 5
a -= 5

from asyncio.format_helpers import _format_callback_source
import math

print(math.ceil(2.2))

# ! Datetime e tempo

from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

strptime -> Transforme str em date, ou data em outros formatos
strftime -> Transforme date em str.

deadline = datetime.strptime(input('Qual o deadline ?'),'%d/%m/%Y')
print(deadline,type(deadline))

#Quantidade de dias ate o seu aniversario
niver = '22/07/2022'
x = datetime.now() - datetime.strptime(niver,'%d/%m/%Y')
print(x)

# ! Valores Aleatorios
import random
print(random.random())
print(random.randint(4,10))
print(random.uniform(4,10))

# Escolha aleatoria uma cor
cores = ['azul','vermelho','verde','amarelo']
print(random.choice(cores), k = 2)  #escolhe 2 valores

# ! DEBUGAR O CODIGO

def calcular_preco_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print(total)

calcular_preco_combo(30,20)
print('\n Programa Finalizado')