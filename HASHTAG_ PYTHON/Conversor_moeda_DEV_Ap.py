
def titulo(txt):
    print('-'*len(txt))
    print(f'{txt}')
    print('-'*len(txt))

def moeda():
    print("1 - BRL \n2 - USD \n3 - EUR \n4 - SAIR")
         
titulo("Programa de Cambio")     

#try: é a operação /except: é quando falhou/exceção / else(opc): operação deu certo / finally(opc): sempre roda

# VALOR INICIAL DE CAMBIO
while True:                 
        try:
            valor_inicial = int(input(
                              "Insira o valor desejado para a operação. \n>> "))
            break
        except:
            print("\nValor indevido, coloque novamente. \n")
                    
#ESCOLHENDO O CAMBIO INICIAL, COM TRATAMENTO DE EXCEÇÕES E ERROS
titulo("Selecione a Moeda Inicial")
moeda_inicial = 0
cod_moeda_inicial = None
while moeda_inicial not in (1,2,3,4):
    moeda()
    try:
        moeda_inicial = int(input("Insira a opção: "))
        if moeda_inicial == 1: 
            cod_moeda_inicial = 'BRL'
            print(f'{cod_moeda_inicial}')
            break
        elif moeda_inicial == 2: 
            cod_moeda_inicial = 'USD'
            print(f'{cod_moeda_inicial}')
            break
        elif moeda_inicial == 3: 
            cod_moeda_inicial = 'EUR'
            print(f'{cod_moeda_inicial}')
            break
        elif moeda_inicial == 4: 
            print('Saindo')
            break
    except: 
        print("\nInserir SOMENTE OS VALORES ABAIXO!")

#ESCOLHENDO O CAMBIO FINAL, COM TRATAMENTO DE EXCEÇÕES E ERROS
titulo('Selecione o cambio de conversão final')
while not in (1,2,3,4):
    moeda()
    #... mesma coisa
    
#4 Conversão
# Aqui utiliza as bibliotecas 
# result = c.convert(cod_moeda_inicial, cod_moeda_cambio, valor_inicial)
# simbolo_moeda = cd.get.symbol(cod_moeda_inicial)
...


  

