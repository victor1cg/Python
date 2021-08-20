# Exercício Python #094 - Unindo dicionários e listas
#a) qtde pessoas b) media de idade c) as mulheres cadastradas d)Lista de pessoas acima da media de idade

galera = list()
pessoa = dict()

soma = media = 0 

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('\nNome: ')).upper()
    pessoa['idade'] = int(input('\nIdade: '))
    soma += pessoa['idade']
    #campo Sexo
    while True:
        pessoa['sexo'] = str(input('\nSexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in "MF":
            break
        else:
            print('\n-=-=-= ERR0 -=-=-= Escreva M ou F')
    
    #add ao dicionario
    galera.append(pessoa.copy())                # a lista recebe uma copia do dicionario
    
    stop = str(input('\nDeseja continuar [S/N]: ')).upper()[0]
    if stop == 'N':
        break
    
    
#print(f'\n{galera}',sep='\n')
print('\n{:-^40}'.format('Respostas'))           #fluff
print(f'\na) A quantidade de registros são {len(galera)}.')
media = soma/len(galera)
print(f'\nb) A média das idades é {media:.2f}.')          # cinco casas ao todo e duas decimais
print('\nc) As mulheres cadastradas foram', end='')
# logica c) e d)
for p in galera:
    if p['sexo'] == 'F':
        a = p["nome"]
        print(f' {a}', end=',')

print(f'\nd) As pessoas que estão com idade acima da média {media} são ')
for d in galera:
    if d['idade'] > media:
        b = d['nome']
        print(f'{b}', end = ',')
        for k,v in d.items():
            print(f'\n{k} : {v}', end='')
        print()
print(f':-^40.format('Encerrado')