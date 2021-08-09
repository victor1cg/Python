# Ex 70 - Programa lê o nome e o preço de vários produtos. 
# 1) total Gasto / 2) Quantos produtos acima de R$ 1000 / 3) produto mais barato
# Interpolação de Strings - antigamente usava .format, hoje troca pelo f"..Texto...{x}'
# Print(f' O {nome} tem {idade} anos.') - fstring > na versão 3.6 acima
# PRint(' O {} tem {} anos' . format(nome,idade)) # aula python 15 - curso em video

total = totmil = cont = menor_val = 0
barato = ""
while True:                                                 #While True é loop infinito
    produto = str(input("\n Nome do Produto:  "))
    preco = float(input("\n Valor do Produto R$: "))
    total += preco                                          # += é igual total = total+preco
    if preco > 1000:
        totmil += 1
    if cont < 1 or menor_val > preco:
        menor_val = preco
        barato = produto

    resp = ' '
    while resp not in "SN":
        resp = str(input('\nQuer continuar ? [S/N] ')).strip().upper()[0]      #a primeira letra sem espaço e maiuscula
    if resp == "N" :
        break
print('{:-^40}'.format('Fim do Programa'))                   #Tratamento de Strings
print(f'\n O total da compra foi de R$ {total:.2f}')
print(f'\n Temos {totmil} produtos acima de R$1.000')
print(f'\n O produto de menor valor é o {barato} no valor de R${menor_val:.2f}')
