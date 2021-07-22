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
