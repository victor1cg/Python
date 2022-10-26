import os

caminho = os.getcwd()
print(os.path.basename(caminho))
print()

#alterando o caminho
if str(os.path.basename(caminho)) != 'docs':
    os.chdir('Dev_Aprender\\08_Automacao\\docs')
    caminho = os.getcwd()
    print(os.path.basename(caminho))
else:
    print('caminho ok !')

#Salva no local definido

#* metodo mais simples
"""with open ('nomes.txt','w') as arquivo:         
    arquivo.write('Nome1') 
"""
#* WRITE APPEND
with open ('nomes.txt','a',newline = '\n') as arquivo:
    nome = ['Abel','Bruno','Costa','Daniel']
    for n in nome:
        arquivo.write(n + os.linesep)

#* READ
with open ('nomes.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)
