#115a - Criando um menu em Python
# Cadastrar um usuario no txt, e verificar todos os cadastrados

from os import system
from colorama import Fore, Back, Style
from time import sleep

galera = []

def exibir_menu():
    print(Fore.BLUE + '''MENU
1) CADASTRO
2) LISTA DE USUARIOS
3) SAIR
''' )
    opcao = int(input("\nDigite a opção desejada: "))
    return (opcao)

def cadastro(): 
    nome = str(input('\nDigite o Nome: '))
    idade = int(input('\nDigite a idade: '))
    return(nome,idade)
    
def cadastro_txt(nome,idade):
        galera.append(nome)
        galera.append(idade)
        

#a = exibir_menu()
#print(a)
b,c = cadastro()
cadastro_txt(b,c)
print(galera)
        
#while True:
#    if a == 1:
        

