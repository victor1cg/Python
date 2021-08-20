#86 - Matriz em Python 
# Crie um programa que produz uma matriz 3x3

matriz = [[0,0,0],[0,0,0],[0,0,0]]              #matriz ja declarada, não precisa usar append, so substitui os zero
spar = maior = scol = 0

for l in range(0,3):                        
    for c in range (0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))

         
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end='')      #:^3 - tres espaços centralizado
        a = matriz[l][c]
        #a) 
        if matriz[l][c] %2 == 0:                    
            spar += a
        #b)A soma dos valores da terceira coluna.
        if c == 2:
            scol += a
        #c)O maior valor da segunda linha.
        if l == 1 and maior < a:
            maior =  a

    print()
print(f"\nA Soma dos numeros pares é igual a :{spar}")
print(f"\nA Soma da terceira coluna é :{scol}")
print(f"\nO maior numero da segunda linha é : {maior}")

                                                #l começa em zero, c começa em zero
                                                #o primeiro input vai na [0][0]
                                                #o segundo input vai na [0][1]> [0][2] > [1][0] > [1][2]
                                                
                                                #a) a soma dos valores pares