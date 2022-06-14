#classes e metodos
# Estudo do Dev Aprender


# __init__ chamado de consultor, serve para os parametros iniciais;
# self - server para acessar os metodos e propriedades da instancia. Podem ser acessadas de outro lugar.
#  
class computador:               #é necessario passar os parametros, se não fica chumbado p/ todos
    def __init__(self, marca,memoria_ram,placa_video):                 
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
        
    def info(self):
        print(self.marca, self.memoria_ram, self.placa_video)

    def Ligar(self):
        print("Estou ligando")
        
pc1 = computador('Asus','8gb','Nvidia')
pc2 = computador('Dell','16gb','Geforce')
pc3 = computador('HP','4gb','Geforce')
pc1.info
#--------- Aula Inicial Python Orientado ao Objeto Boson

class Cubo: 
        '''Criar uma classe que calcula o valor do cubo'''
        def __init__(self,valor):
            self.x = valor                    # com o self a variável x é global / Metodo construtor
            print('Objeto criado!')
        
        def calcula_cubo(self):
            cubo = self.x ^3
            return '\n Cubo calculado:' str(cubo)
teste = Cubo(6)                               #objeto teste recebe todo o comando de Cubo, porém so executa o __init__
c = teste.calcula_cubo                        # c é a variavel que chama a função calc_cubo
print(c)
R: Objeto Criado!
   Cubo calculado : 216

#---------- EX 3
class gato:                             
    tipo_animal = "Felino"                  #chumbando que sempre será Felino
    
    def __init__(self,nome):                #inicializa o objeto capturando o nome
        self.nome = nome
        print('Seu gatinho se chama',self.nome)
        
    def info(self, peso):                   #definir as funções e depois definir os inputs
        self.peso = peso
        #self.raca = raca
        #self.idade = idade
        if(self.peso > 5.0):
            print(f'Seu gato {nome_gato} esta gordo')
        else:                                   #se tive uma 3ª coloca ELIF:
            print(f'Seu gato {nome_gato} está OK!')
            
nome_gato = input('Digite o nome do seu gato \n')
g1 = gato(nome_gato)                            #objeto G1 é uma instancia da classe gato

peso_gato = float(input('\n Qual o peso do gato ? \n'))  
g1.info(peso_gato)                              #chama o metodo info e passa a variavel peso
