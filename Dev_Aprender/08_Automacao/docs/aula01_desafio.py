# Primeiro crie 3 listas
'''
 * Uma lista que contem 5 frutas
 * Uma lista que contem 5 cores
 * Uma lista que contem 5 linguagens de programação
'''
from mailbox import linesep
import os
frutas = ['Fruta1', 'Fruta2', 'Fruta3', 'Fruta4', 'Fruta5', ]
cores = ['Cor1', 'Cor2', 'Cor3', 'Cor4', 'Cor5']
linguagens = ['Python', 'C#', 'Javascript', 'Java', 'PHP']
os.chdir('Dev_Aprender\\08_Automacao\\docs')

""" #! Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open ('frutas.txt','a',newline='\n') as arquivo:
    for f in frutas:
        arquivo.write(f + os.linesep)

#! Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('frutas.txt','r') as arquivo:
    for f in arquivo:
        print(f) """
#! Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('frutas.txt','a',newline='') as arquivo:
    for f in cores:
        arquivo.write(f + os.linesep)
#! Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linguagem ocupe apenas uma linha.

#! BONUS - Como você poderia criar vários arquivos vazios, usando um laço for?
arquivos = ['musica.mp3','anotacoes.txt','requirements.py']

for a in arquivos:
    with open[a,'w']:
        pass