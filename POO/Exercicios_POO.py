# exerciciso de POO Python

class Gato:                                     #definir a classe
    '''Classe para trabalho com info do gato'''
    def __init__(self,nome,peso):               #metodo construtor automatico
        '''Inicializa capturando o nome'''
        self.x = nome,
        self.y = peso,
        print(f'O gato {self.x} está com o peso {self.y} !')
                                                #1 - classe instanciada
nome_gato = input('\n Qual o nome do gato ?\n')
g1 = Gato(nome_gato)                            #2 - variavel que sera utilizada no parametro

peso_gato = float(input(f'\n Qual o peso do gato {nome_gato} ?\n'))
g2 = Gato(peso_gato)                            