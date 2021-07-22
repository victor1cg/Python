import PySimpleGui as sg

class TelaPython:                       #criar uma tela com Nome:input | Idade: input | Enviar (temos 5 campos)
        def __init__(self):
            #layout
            layout = [
                [sg.Text('Nome'),sg.Input()]       #cada linha é uma linha no desenho
                [sg.Text('Idade'),sg.Input()]
                [sg.Button('Enviar Dados')]
                
             #janela
            janela = sg.Window("Dados do usuario").layout(layout)
        
            #extrair os dados
            self.button,self.values = janela.Read()     #metodo para obter os dados
        
        def iniciar(self):                          #importante para organizar melhor
            print(self.values)
   
tela = TelaPython()
tela.iniciar()