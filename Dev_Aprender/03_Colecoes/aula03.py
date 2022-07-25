
#! Dicionarios

pessoa = [dict(nome = 'Carol',idade = 40, cidade = 'SP'),
             dict(nome = 'Pedro',idade = 40, cidade = 'SP'),
             dict(nome = 'AYZ',idade = 33, cidade = 'PR'),
             dict(nome = 'Jones',idade = 40, cidade = 'CB')]

""" print(pessoa[0].keys())
print(pessoa[0].values())
print(pessoa[0].items())

for item in pessoa.items():
    print(item[0])
 """
#*SORT values - ITEMGETTER
from operator import itemgetter

pessoa.sort(key=itemgetter('nome'), reverse = True)
# print(pessoa)

# tupla ou lista de lista consigo sort pelo indice
matriz = [[2,15],[4,5],[10,9]]
matriz.sort(key=itemgetter(1)) 
# print(matriz)


#! Tuplas - não é tipado, é imutavel, e ordenado.

#! Array - É tipado, somente do mesmo tipo!
""" from array import array
# int,float, str
numeros = array(i,[1,2,3,4,5,6])
numeros.append(10)
numeros.insert(8,2)
numeros.pop(1)
del numeros(1) 
numeros.remove(5) """

#! Listas - ENUMERATE - percorrer a lista, onde estamos atualmente
#sempre retorna um indice e o valor real. Indice começa em 1

""" for i,v in enumerate(pessoa):
    print(i,v) """

