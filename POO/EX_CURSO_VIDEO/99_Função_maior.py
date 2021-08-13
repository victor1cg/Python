# 99 - Exercício Python #099 - Função que descobre o maior

def maior_valor(*num):
    cont = a =0
    for n in num:
        if cont == 0 or n > a :
            a = n
            cont += 1
        else:
            cont += 1
    print(f"\n O total de numeros da lista é {cont}, e o maior numero é {a}")

#lista = [1, 2, 10, 5, 20]
maior_valor(1, 2, 40, 5, 20)

# 104 - Validação de dados input

def ficha(jog = "<desconhecido>", gol=0):               #colocando os parametros opcionais
    print(f"\nO jogador {jog} fez {gol} gol(s) no campeonato.")


n = str(input("\nNome do Jogador:  "))
g = str(input("\nQuantidade de Gols:  "))

if g.isnumeric():
    g = int(g)
else:
    g = 0
    
if n.strip() == '':            #strip remove spaces|lstrip|rstrip > a = !!Hello!! > a.strip("!") > Hello 
    ficha(gol=g)                # faz a chamada da função somente com o parametro g 
else :
    ficha(n,g)                  # faz a chamada do parametro ficha