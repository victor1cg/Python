
#* 01 Metodos Comuns - utiliza self; Precisa instancia para buscar os dados.

#* 02 Metodos de Classes (Class Methods) - utiliza cls. pode mudar a implementação, 
#           ou seja, pode ser reescrito pela classe filha

#* 03 Metodos Estaticos (Static Methods) - não podem ser reescritos pelas filhas, 
#           já que são imutáveis e não dependem de um referência especial.

import time
class Computador:
    sistema_op = 'windows 10'

    def __init__(self,marca,memoria,placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video

    def ligar(self):
        print('Estou ligando..')
        time.sleep(3)

    def exibir_dados(self):
        print(f'Computador da marca {self.marca}, memoria de {self.memoria} e placa {self.placa_video}')

#! 02 - Has 2 types of computer config, office and games.
#somente a memoria sera definida pelo user, outros atributos ficam padrão.
    @classmethod
    def computador_office(cls, memoria):
        return cls('Dell', memoria,'Placa de video interna')
    
    @classmethod
    def computador_game (cls,memoria):
        return cls('Dell', memoria,'Placa Nvidia')

#! 03 - Static dont use methods with self__. Also dont use cls.
# Não deixar funções soltas. Faz sentido deixar ela dentro da classe.
    @staticmethod
    def roda_programa_pesado (memoria):
        if int(memoria) >8:
            return True
        else:
            return False



""" #office
pc = Computador.computador_office('8 Gb')
#games
pc2 = Computador.computador_game('16 Gb')

pc.exibir_dados()
print('')
pc2.exibir_dados() """

#Static
pcx = Computador.computador_office('12')
print(pcx.marca)
print('')
print(Computador.roda_programa_pesado(pcx.memoria))





