#exercicio do Dev Aprender

from os import system
from time import sleep
from 1_cabecalho import Formatar_menu

class Carro:                               #classe sempre começa com maiuscula
    def __init__(self,marca,ano,motor):
        self.marca = marca
        self.ano = ano
        self.motor = motor
    
    
    def ligar(self):                        #outro metodo
        print('\nLigando carro!')
    
    def infos(self):                        #todas as propriedades de dentro do self, podem ser atribuidas
        print(self.marca,self.ano,self.motor)
    
carro_mae = Carro('Nissan','2019','1.0')    #criando a instancia da classe
carro_mae.ligar()
carro_mae.infos()                           #chamando as propriedades
sleep(2)
print('Desligando carro')
Formatar_menu('Novo Cadastro','Verificar Cadastro','Sair')
#system('cls')                               #limpar o terminal
