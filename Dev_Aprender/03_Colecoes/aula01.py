
#! LISTAS

precos = [10,20,30,40,50,60,80,55,69,25]
print(precos[1]) #Indice
print(precos.index(25)) #acha o valor, retorna o indice

#* Multiplicação de valores
lista_de_noves = [9]*10
print(lista_de_noves)

#* Usando gerador range
faixa_numeros = list(range(20))
print(list('Cavalo'))

#* Lista de Lista
matriz_nomes = [['Carol',30],['Marcos',28]]

#* Adicionando valores
valores = [1,2,4]
anos = [2020,2021,2022]
#Adicionar ao final da lista
valores.append(11)

#Unir listas /porem não cria uma nova, modifica a existente
valores.extend()
#Juntar duas lista, e criar uma nova:
nova_lista = valores + anos

#Inserir um novo valor. (indice,valor)
anos.insert(2,2031)

#Deletar com base no indice
anos.pop(0)
del anos[0]             #Aqui podemos passar uma faixa de valores [1:3]
#Deletar com base no valor
anos.remove(2020)
#Resetar os valores de uma lista
anos.clear()

#Contar a qtde de ocorrencias
anos.count(2)           #qtde de vezes que aparece o numero 2