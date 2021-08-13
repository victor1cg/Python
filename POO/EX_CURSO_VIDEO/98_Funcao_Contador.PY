#Funcao_Contador_98 - Colocar inicio/ fim / step
def contador(i,f,s):
    i = input("\nColoque o numero inicial  ")
    f = input("\nColoque o numero final    ")
    s = input("\nColoque o step desejado   ")
    pos = 0
    a = range (i,f,s)
    print(list(a))      

contador()

# de 1 ate 10, de 1 em 1
def contador2(i,f,s):
    cont = i
    while cont <= f :
        print(cont, end="")
        cont += s
    print('FIM')

contador2(1,11,1)