
#! CSV
# r	- Read (default)	Open a file for read only
# w	- Write	Open a file for write only (overwrite)
# a	- Append	Open a file for write only (append)
# r+ -	Read+Write	open a file for both reading and writing
# x - Create	Create a new file

# Because read mode ‘r’ and text mode ‘t’ are default modes, you do not need to specify them.

#* Raw mode:
# path = (r'Dev_Aprender\08_Automacao\docs\aula04_csv.csv')
""" with open(path) as arquivo:
    dados = arquivo.read()
    print(dados)
 """

#*Using library
from csv import DictReader,DictWriter
""" 
path2 = (r'pessoas.csv')
file = open(path2)
with file:
    dados = DictReader(file)
    for dado in dados:
        print(dado['Nome'] +' '+ dado['Idade']) 
 """
#*Criar um arquivo CSV
""" new_file = open('computadores.csv','w',encoding='utf-8')
with new_file:
    header = ['Marca','Preco','Data']
    csv_w = DictWriter(new_file, fieldnames= header)
    csv_w.writeheader()
    csv_w.writerow({
        'Marca': 'Asus',
        'Preco':1499,
        'Data': '01/01/2018'
    })
    csv_w.writerow({
        'Marca': 'HP',
        'Preco':1899,
        'Data': '01/01/2021'
    })
 """
#*Alterar um arquivo CSV (colocar R$ em preco):
#salvar numa lista dados do csv antigo
with open('computadores.csv','r') as old_file:
    old_data = DictReader(old_file)
    computadores = list(old_data)

#criar um novo csv
with open('computadores.csv','w') as new_file:
        header = ['Marca','Preco','Data']
        csv_w = DictWriter(new_file, fieldnames=header)
        csv_w.writeheader()

#loop para cada dado in computadores:
        for comp in computadores:
            csv_w.writerow({
                'Marca' : comp['Marca'],
                'Preco' : ('R$ ' + comp['Preco']),
                'Data': comp['Data']
            })
# for n in range(len(pc)):
#     print(pc[n].values())

# with file:
#     dados = DictReader(file)
#     for dado in dados:
#         print(dado['Nome'] +' '+ dado['Idade']) 
    # old_data = DictReader(old_file)
    # pc_preco = []
    # for data in old_data:
    #     pc_preco.append('R$ ' + data['Preco'])                 #lista de dicionario
    # print(pc_preco)
