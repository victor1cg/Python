# Funções utilizadas

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
    return valor                         


def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n*2


def triplo(n):
    return n*3
