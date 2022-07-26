
#! 01 VARIAVEIS

from numpy import dtype

velocidade = 10

a, b, c, d = 1, 1, 3, 4

# print(type(b))
# print()
# print(velocidade)

#! 02 Ambiente -
"""Ir na pasta do arquivo .py, e segurar o shift + Mouse(esquerdo) -> Abrir Power Shell
   No Power Shell: ls ; python aula01.py
"""

#! 03 Indentação
if a > b:
    print(a)

elif b > a:
    print(b)

else:
    print(
        """iguais 
        os valores"""
    )

#* Caracteres de escape
"""print("\nCaracteres de espaço \n pula linha")
print("\nA barra invertida considera 'o caracter")     # Aqui uma barra invertida
print("\nArquivo localizado em C:\\usuario\\scripts")  # Aqui uma barra invertida
print(r"\\nArquivo localizado em C:\\usuario\\scripts")   # Aqui o r considera tudo como literal """

#* String Dinamico
nome = "Cavalo"
email = "victor@hotmail.com"
print(f"Ola {nome} voce colocou o email : {email}")

#! 04 Metodos comuns String
nome_curso = "  data Science  ! "
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip().capitalize())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find("!"))
print(nome_curso.replace("data", "lata"))
print(r"http:olx.com.br/produtos=carro".replace("carro", "patinete"))

# utilizando diretamente
aa = "frase"
bb = "de"
cc = "efeito."
print(f"{aa.capitalize()} {bb} {cc.upper()}")


#! PRINT - Substituição
#* % - Esse aqui veio do Python 2
print('A programação em %s é muito mais %s' % ('python','facil'))
print('A programação em %(a)s é muito mais %(b)s' % {'a':'python','b':'facil'})
# 0.1 casa decimal
print('A programação em %(a)s possui %(b).1f anos' % {'a':'python','b':14.5})

#* .format - Esse é Python 3
print('A programação em {} possui {:.1f} anos' .format('python',14.5))
