
#! CLASSE ABSTRATA
# Um método abstrato é um método que possui uma declaração, 
# mas não possui uma implementação. Obrigado a classe filha a implementar.

#* DESAFIO - Classe abstrata chamada Monitor com 2 metodos:
# > aumentar_claridade | reduzir_claridade.
# > Criar a Classe Filha > monitor Full HD; > Devemos passar o valor atual do brilho, 
# e o quanto queremos aumentar/diminuir.

from abc import abstractmethod


class Monitor:                              #atributo da classe monitor somente qtde atual de brilho
    def __init__(self,qtde) -> None:
        self.qtde = qtde
    @abstractmethod
    def aumentar_claridade(self,qtd):
        pass
    @abstractmethod
    def diminuir_claridade(self,qtd):
        pass

class monitor_fullHD(Monitor):              
    def __init__(self,qtde):
        super().__init__(qtde)

    def aumentar_claridade(self,qtd):
        self.qtde += qtd
        return (f'Claridade aumentou para {self.qtde}')
    
    def diminuir_claridade(self,qtd):
        self.qtde -= qtd
        return (f'Claridade diminui para {self.qtde}')

monitor = monitor_fullHD(100)
print(monitor.aumentar_claridade(10))
# print(monitor.qtde)