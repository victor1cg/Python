from numpy import NaN
import pandas as pd
import os


df_p = pd.read_excel(r'Data_Analyses\python.xlsx',header=0)
df_c = pd.read_excel(r'Data_Analyses\cienciadados.xlsx',header=0)


##--- Tabela CONCAT ---##
#Necessario ser uma lista de tabelas
#Concat usa o header com mesmo nome, mas mantem o index

lista_tabelas = [df_p,df_c]

tab_concat = pd.concat(lista_tabelas,ignore_index = True)
tab_concat2 = pd.concat(lista_tabelas,keys = ['py','ciencia']) # o primeiro indice é origem da tabela, não consigo usar ignore_index


##--- Tabela MERGE ---## Quase que um procv
# Descobrir quais clientes compraram os dois produtos

tab_produtos_inner = pd.merge(df_p,df_c, on = 'Cliente')
tab_produtos_left = pd.merge(df_p,df_c, on = 'Cliente', how= 'left')
tab_produtos_left = tab_produtos_left[tab_produtos_left['Parcelas_x']==12.0]
print(tab_produtos_left)
