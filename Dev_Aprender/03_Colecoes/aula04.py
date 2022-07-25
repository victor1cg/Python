
#! MAP - Processando itens de uma lista
#* Criar lista usando loop - MAP não precisa de FOR!!!
""" numeros = []
for i in range(5):
    numeros.append(i)
print(numeros) """

#1) Usando MAP - função sera aplicada a todos os itens da lista
nomes = ['A','B','C','D']
def aprovar_pessoas (nome):
    return nome + ' Aprovado'

#print(map(aprovar_pessoas,nomes)) #desse jeito não funciona, pois retorna uma função, necessario jogar numa lista
# print(list(map(aprovar_pessoas,nomes)))

#2) Usando MAP - Somar duas lista
a = [1,2,3]
b = [4,5,6]

x = map(lambda x,y: x+y,a,b)
print(list(x))

#* ​DESAFIO -  Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.

pinturas = [['Pintura Classica', 'Azul', 1857],
['Pintura Medieval', 'Vermelha', 1867],
['Pintura Moderna', 'Verde', 1897]]

cores = []
def extrair_cores(pint):        #*não precisei utilizar o for para percorrer os itens da lista.
    a = pint[1]
    cores.append(a)
    return cores

print(list(map(extrair_cores,pinturas)))

#! Filter
# retornar apenas os dados verdadeiros (return True), parecido com MAP().
# Pois, podemos substituir o loop.

nomes = ['Larissa','Joao','Carlos','Antonio']
def aprovados(nomes):
    if nomes == 'Carlos':
        return True
    else:
        return False

""" print(list(filter(aprovados,nomes)))
#>> ['Carlos']
print(list(map(aprovados,nomes)))
#>> [False, False, True, False]
 """
#2)
pinturas = [['Pintura Classica', 'Azul', 1857],
['Pintura Medieval', 'Vermelha', 1867],
['Pintura Moderna', 'Verde', 1897]]

def antiguidade(pintura):
    if pintura[2] > 1870:
        return True
    else:
        return False

print(list(filter(antiguidade,pinturas)))