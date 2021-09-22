#Formatar menu  
from os import system
from time import sleep

def Formatar_menu(*num):
    print('-'*30)
    print(f'{"CONSULTA":^30}')                              #centralizar o Cabeçalho em 30 caracteres
    print('-'*30)
    for n in range(0,len(num)):
        print(f'{[n]} {num[n]}')

Formatar_menu('Novo Cadastro','Verificar Cadastro','Sair')
#system('cls')