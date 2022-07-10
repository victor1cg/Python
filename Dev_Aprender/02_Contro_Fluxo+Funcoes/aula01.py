for numero in range(20):
    if numero % 2 == 0:
        print(numero)
    else:
        continue        #ou podemos usar pass

# ! FUNCOES

#*SEMPRE variaveis com valor default devem ser passadas no final
def apresentar_lugar(horario, lugar = 'Miami'):          
    print(f'Conheca {lugar}! No horario {horario}')      #por default temos Miami, 

apresentar_lugar('Disney')                               #nesse caso print Disney


def exibir_preco(produt,preco):
    print(f'{produt} esta no valor de {preco}.' )

#Argumentos Posicionais
exibir_preco('Iphone',4500)

#Argumentos Nomeados
exibir_preco(preco=4800,produt='Samsumg')

#* Podemos obrigar a ser argumento obrigatorio com o *
def exibir_preco2(produt,*, preco, origem='China'):
    print(f'{produt} esta no valor de {preco}. Origem {origem}' )

exibir_preco2('Iphone',preco = 1000)