#Exercício Python #104 - Validando entrada de dados em Python

def leia_int(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\nErro! Digite um numero inteiro válido!')
        if ok:
            break
    return valor                            #retorna o valor para o ultimo print    


a = leia_int('\n Digite um numero  ')
print(f'\n Voce digitou o numero {a}.')

# exercicio do fatorial

def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

a = int(input('\n Coloque um Numero para saber seu fator  '))
fat = fatorial(a)
print(f"\n O fator do numero {a} é {f}")