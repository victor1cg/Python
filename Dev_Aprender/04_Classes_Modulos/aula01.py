
#! 01 - MODULOS

# isso aqui já é um MODULO - É um arquivo python normal.

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
    print(f'Estamos no arquivo {__name__}\n')


#* ----------- Atributos de uma CLASSE 
# self >> é importante pois ele permite acessarmos de qualquer lugar esse atributo.
# Classe Pessoa . Fabio é uma instancia de Pessoa. Fabio tem atributos e metodos;
import time
class Computador:
    #variaveis de classe é possivel modificar        
    sistema_op = 'windows 10'

    #variaveis de instancia - são padronizadas
    def __init__(self,marca,memoria,placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video

#* ----------- Metodos de uma CLASSE
    def ligar(self):
        print('Estou ligando..')
        time.sleep(3)

    def exibir_dados(self):
        print(f'Computador da marca {self.marca}, memoria de {self.memoria} e placa {self.placa_video}')

computador1 = Computador('Dell','32 Gb','Nvidia')
# computador1.ligar()
# computador1.exibir_dados()


#variaveis de classe -> Computador.marca ñ funciona, primeiro instancia para buscar a propriedade;        
print(computador1.marca)
print(Computador.sistema_op)

Computador.sistema_op = 'Linux'         #fica chumbado Linux
print('\n'+ Computador.sistema_op)
