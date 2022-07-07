'''
Uma Classe (atrib + metodos) -> Objeto1 (atrib + metodos) ; Objetos2 (atrib + metodos); etc
'''
# Exercicio criando um sistema da Netflix

class Cliente:
    def __init__(self,nome,email,plano):
        self.nome = nome                        #Atributos
        self.email = email
        self.plano = plano
        self.planos = ['basico','premium']
        
        if plano in self.planos:
            self.plano = plano
            print(f'\nO plano é {plano}')
        else:
            raise Exception('\nPlano inválido!') #Caso o plano não esteja na lista


    def mudar_plano(self,novo_plano):           #funçoes
        if novo_plano in self.planos:           #como atribui o self.planos, consigo utilizar dentro da classe
            self.plano = novo_plano
        else:
            print('Plano inválido')

    def ver_filme(self,filme,plano_filme):      #caso o filme seja para diferentes planos.Premium roda todos os filmes.
        if self.plano == plano_filme:
            print(f'\nPlay filme {filme}')
        elif self.plano == 'premium':
            print(f'\nPlay filme {filme}')
        elif self.plano == 'basico' and plano_filme == 'premium':
            print('\nRealizar upgrade para Premium!\n')
        else:
            print('\nPlano invalido!')


### Importante. Uma variavel recebe a classe, e portanto usamos as funções e atributo 
cliente = Cliente('Victor','victor@gmail.com','premium')            #INSTANCIAR a CLASSE Cliente para o OBJETO cliente 
#print(cliente.plano)                           #printar os atributos

cliente.ver_filme('Top Gun','basico')                               #acessar o OBJETO cliente, e invoca o metodo


####-------- 2) --------####
# exercicios de POO Python- Boson

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
