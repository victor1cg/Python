#Funcoes_Curso_Video - Curso Python #20 - Funções (Parte 1)

def mensagem(msg):                              #aqui é possivel passar um parametro
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem('O TESTE FUNCIONA')
#------------
def soma(a,b):
    s = a + b
    print(s)
    
soma(4,5)

#------------
def contador(*num):                             #quantidade ilimitada de parametros
    a = len(num)
    print(a)
    
contador(2,3,4,5,6)
#------------
def dobra_valor(*num):                          #dobra valor por desempacotamento
    for n in num:
        a= n*2
        print (a)

dobra_valor(2,3,7)
#------------
def dobra_valorr(lst):                          #nesse caso ele modifica a lista valores
    pos = 0                                     
    while pos < len(lst):
        lst[pos] *= 2                           #o que fizer em lst, vai modificar valores 
        pos += 1
        
        
valores = [2, 3, 4, 5]
dobra_valorr(valores)
print(valores)