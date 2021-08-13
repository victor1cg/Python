# a) Os 5 primeiros  b) Os ultimos 4  c) Times em ordem Alfabetica  d) Posição da Chapecoense

lista_times = (
'Flamengo','Palmeiras','Corinthians','Atlético-GO','Sao Paulo','Fluminense','Atlético-MG',
'Fortaleza','Internacional','Sport','Ceará','Grêmio','Bahia','Santos','Chapecoense','Red Bull Bragantino'
)

#for t in lista_times:
#    print(t)
#print("=-" *30)

#print('Os ultimos 4 times são:\n')
#print(lista_times[-4:])

#print('Os times em ordem são:\n')
#print(sorted(lista_times))

time_busca = str(input('Escreve o nome do time\n'))
index_busca = lista_times.index(time_busca) + 1
print(f'\n O time {time_busca} está na posição {index_busca}')