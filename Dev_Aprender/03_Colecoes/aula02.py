
#! LISTA_Cont

## SORT A LIST OF LISTS
from operator import itemgetter
A = [[10, 8], [90, 2], [45, 6]]
print("Sorted List A based on index 0: % s" % (sorted(A, key=itemgetter(0))))

#Lambda
A = [[100, 'Yes'], [40, 'Maybe'], [60, 'No']]
print("Sorted List A based on index 0: % s" % (sorted(A, key=lambda x:x[0])))

#>>Sorted List A based on index 0: [[10, 8], [45, 6], [90, 2]]

#! Multiplas Listas

#* ZIP - Consigo trabalhar em duas+ listas ao mesmo tempo
# Caso as lista tenha o mesmo len, usar zip. Senão, necessario usar zip_longest
from itertools import zip_longest

precos = [10,20,30,40,50,60,80,55,69,25]
produtos = ['PC','TV','SOM','Washing','Cooling']

for a,b in zip_longest (precos,produtos):   #somente print das infos necessarias
    if b == None:
        continue
    else:
        print(f'Salvando o produto {a}, valor {b}')

