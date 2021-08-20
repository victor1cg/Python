# -=-=-=-=- Sistema de login em Python -=-=-=-=-

from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
from time import sleep

init(autoreset= True)   

#criar a o menu de opções

def exibir_menu():
    print(Fore.GREEN + ''' Bem Vindos ao projeto 
 Sistema de Login
 Escolha um opção:
[1] Cadastrar novo usuario
[2] Fazer Login
[3] Sair
          ''')
    opcao = int(input('\nDigite a sua opção: '))
    return(opcao)

def fazer_login():
    login = str(input('\nNome : '))
    senha = str(input('\nSenha: \n'))
    return(login,senha)

def buscar_usuario(login, senha):           #necessario para login 1
    usuarios = []
        with open('users_sistema.txt', r+, encoding='Utf-8',newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                                 
                
#Cadastrar novo usuario
login,senha = fazer_login()                 #recebo duas variaveis
if login == senha:
    print(Fore.RED+ "Usuario já existente")

user = buscar_usuario(login,senha)
if user == True:
    print()


a = exibir_menu()
print(a)
b = fazer_login()
print(b)

#while True:
#    system('cls')
#    opcao = exibir_menu
    
    