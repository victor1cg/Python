
#! MANIPULANDO ARQUIVO TXT
""" 
r - Usado somente para ler arquivos
w - Usado somente para escrever algo
r+ - usado para ler e escrever algo
a - usado para acrescentar algo """

telefone = [11111,22222,33333,44444,55555]

# ESCRVER ARQUIVO
# with open ('arquivo.txt','a') as arquivo:
#     for valor in telefones:
#         arquivo.write(str(valor)+ '\n')

#LER O ARQUIVO
# with open ('dados.txt','r') as arquivo:
#     for valor in arquivo:
#         print(valor)

#LER E ALTERAR
with open ('dados.txt','r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')

