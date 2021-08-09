#Emprestimo bancário - Pergunte o valor da casa, o salario do comprador e a qts anos.
#A prestação não pode passar 30% do salario

valor_casa = float(input('\n Qual o valor da casa?\n'))
salario = float(input('\n Qual o valor do seu salario ? \n'))
anos = int(input('\n Em quantos anos será o emprestimo ?\n'))
parcela = valor_casa/(anos*12)
minimo = salario * 30/100
print('\nPara pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos))
print(', a prestação será de R${:.2f}\n'.format(parcela))

if parcela <= minimo:
    print('\n Emprestimo CONCEDIDO')
else:
    print('\n Emprestimo NEGADO')

