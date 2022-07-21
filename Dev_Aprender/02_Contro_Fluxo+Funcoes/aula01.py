
# ! LOOP
for numero in range(20):
    if numero % 2 == 0:
        print(numero)
    else:
        continue        #ou podemos usar pass

# ! FUNCOES

#todo SEMPRE variaveis com valor default devem ser passadas no final
#1)
def apresentar_lugar(horario, lugar = 'Miami'):          
    print(f'Conheca {lugar}! No horario {horario}')      #por default temos Miami, 

apresentar_lugar('Disney')                               #nesse caso print Disney

#2)
def exibir_preco(produt,preco):
    print(f'{produt} esta no valor de {preco}.' )

#todo Argumentos Posicionais
exibir_preco('Iphone',4500)

#todo Argumentos Nomeados
exibir_preco(preco=4800,produt='Samsumg')

#3)
#todo Podemos obrigar a ser argumento obrigatorio com o *. 
#O que estiver antes OBRIGATORIO(produt)
def exibir_preco2(produt,*, preco, origem='China'):
    print(f'{produt} esta no valor de {preco}. Origem {origem}' )

exibir_preco2('Iphone',preco = 1000)

def gerar_objeto_personalizado(cor,*,altura = None,formato = None):
    print(f'O produto {cor} tem altura {altura} e formato {formato}')

gerar_objeto_personalizado('vermelho',altura = 1.90, formato = 'redondo')

#*4) ARGS > *args | POSICIONAL
# Recebe na forma de tupla (10,20,25...)
def somar(*valores,b=0):
    for valor in valores:
        b += valor
    print(b)

somar(10,20,25,b=5)    #b precisa ser argumento nomeado

#*5) KWARGS >  **kwargs (keyword arguments) | NOMEADO
#kwargs recebe na forma de dicionario
def concatenar(**kwargs):
    frase = ''
    for palavra in kwargs.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nos',b='Somos',c='Python')

#!6) JUNTANDO ARGS E KWARGS
def fazer_calculo(nome,*args,**kwargs):
    print(nome)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('jeff',1,2,3,4,5,a=6,b=7,c=8,d=9)