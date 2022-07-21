# link com o script - https://pastebin.pl/view/68f5bec0

import sys
import random

#email sera criado apartir do nome
# emails = ['a','b','c','d','e']
# nomes = ['Felipe', 'Joao','Daniel','Vitor','Maria']
telefone = [11111,22222,33333,44444,55555]
cidade = ['SP','RJ','BH','PO','CW']
estado = ['SP','RJ','MG','RS','PR']


#input dos nomes 
def input_nomes():
    a = 0
    nomes = []
    print('\nInsira o nome de 5 funcionarios!\n')
    while a < 5:
        nome = input(f'{a} : ')
        a += 1
        nomes.append(nome)
    return nomes

#cria os emails com base nos nomes
def criar_email(*nomes):
    emails = []
    nomes = nomes[0]
    for n in nomes :
        a = n.strip().replace(" ","").lower()+('@gmail.com')
        emails.append(a)
    return emails

nomes = input_nomes()                               #input dos nomes    

#* 1 - Quais dados o user precisa ? Printar na tela.
# nomes = ['Guido', 'Joao Hader','Felipe','Vitor','Elux']
def print_dados(*args):
    x = random.randint(0,4)
    dados_salvos = []               #aqui sera salva as informacoes
    args = args[0]
    for n in args:
        if n == '1': 
            print (nomes[x])
            dados_salvos.append(nomes[x])
        elif n == '2': 
            print (emails[x])
            dados_salvos.append(emails[x])
        elif n == '3': 
            print (telefone[x])
            dados_salvos.append(telefone[x])
        elif n == '4': 
            print (cidade[x])
            dados_salvos.append(cidade[x])
        elif n == '5': 
            print (estado[x])
            dados_salvos.append(estado[x])
        elif n in ('Parar','PARAR','parar'):                #argumento que stopa o programa
            print('\n---- Finalizando o programa. ----')
            sys.exit()
        else:
            print ('\n Insira um valor valido de 1 a 5')
    return dados_salvos

def info_desejadas():
    info = input('''
-------------
Bem-vindo ao gerador de dados de Teste - Para finalizar o programa , digite 'Parar'.
-------------
Escolha uma ou mais opcoes abaixo a serem geradas aleatoriamente:
[1] - Nome
[2] - E-mail
[3] - Telefone
[4] - Cidade
[5] - Estado
Digite uma ou várias opcoes entre virgulas !:\n
''')
    return info



#* 2 - O user deseja salvar em txt ?
# dados.txt

#salva as informacoes selecionadas no dados.txt
def salva_dados(x):
    x = str(x).lower()
    if x == 'y':
        with open('dados.txt','a') as arquivo:
            for dado in dados_salvos:
                arquivo.write(str(dado) + '\n') 
    elif x == 'n':
        pass

#pergunta se o user quer salvar as informacoes
def info_salvas():                      #somente sai da função inserindo Y ou N
    a = ''
    while a not in ('y','n','Y','N'):
        a = input('\n Deseja salvar as informacoes em txt ? [Y/N] : ')
    return a

emails = criar_email(nomes)                         #utilizo o return do input_nomes no criar_email. Porem resultado vem como tupla.
  
#* 3 - Digitar 'parar' finaliza o programa
# inserido uma clausula no if

# todo 4 - Novos dados devem ser append ao anterior
while True:
    info = str(info_desejadas()).split(',')             #transformar o input em lista
    dados_salvos = print_dados(info)          #lista com os dados printado que podem ser salvo em txt
    salva_dados(info_salvas())                          #
