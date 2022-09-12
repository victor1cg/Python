
#! 01 - MODULOS

# isso aqui já é um MODULO - É um arquivo python normal.
import datetime

#! 02 - Quando usar modulos ? 
# Separar funcionalidades relacionadas.
# Manter organização, e não deixar o programa muito longo.

#! 03 - O que é um Pacote ?
# Diversos modulos reunidos. 
# Todo PACOTE possui um arquivo __init__.

#! 04 - Utilizando um pacote:
# Todo arquivo armazena uma variavel __name__.

if __name__ == '__main__':
    print('Ligando o carro!')
    print(f'Estamos no arquivo {__name__}')

