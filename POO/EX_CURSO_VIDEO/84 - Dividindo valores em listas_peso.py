# 84 - Dividindo valores em listas
#Programa que recebe nome e peso: a) Qtde de pessoas cadastradas b) Os 2 mais pesados c) os dois mais leves



def cadastra_peso():
    dado = list()
    galera = list()
    qtde = maiorp = menorp = int()
    nome_maiorp = nome_menorp = x = ""

    while True:
        nome = str(input("Nome: "))
        peso = int(input("Peso: "))
        x = str(input('Deseja Encerrar [S/N]: ')).upper()[0]

        dado.append(nome)               #colocar na lista dado
        dado.append(peso)               
        galera.append(dado[:])          #colocar na lista galera
        dado.clear()
        
        
        if  qtde == 0 :
            maiorp = menorp = peso
            nome_maiorp = nome_menorp = nome
            
        if  peso > maiorp:
            maiorp = peso
            nome_maiorp = nome
        
        if  peso < menorp:
            menorp = peso
            nome_menorp = nome 

        qtde += 1
        if x == 'S':
            break
    print(f'\nO total de pessoas é {qtde}')
    print(f'O maior peso é {maiorp} do {nome_maiorp}.')
    print(f'O menor peso é {menorp} do {nome_menorp}.') 
    print(galera)   
        
a = cadastra_peso()     

