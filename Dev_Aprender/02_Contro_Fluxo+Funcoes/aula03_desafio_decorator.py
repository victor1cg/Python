''' 
Crie um decorator que irá pegar a função que for passada para ele e imprimir o horario antes
de executar, e depois que executar. 
'''

from datetime import datetime

def meu_decorator(f):
    def wrapper():
        print(datetime.now())
        f()
        print(datetime.now())
    return wrapper

@meu_decorator
def teste():
    print('teste')

teste()

# * f recebe a função teste| wrapper retorna a função meu_decorator.wrapper| 
# * teste() recebe também o wrapper(meu_decorator.wrapper).
# * roda a função print > f > print. 