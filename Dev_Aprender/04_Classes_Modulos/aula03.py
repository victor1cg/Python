
#! HERANÇA SIMPLES
# Conseguimos reutilizar a class Camera para um tipo espeficico de camera.
# Não é necessario criar novamente toda a classe. 
# Implicitamente todas classe tem uma herança de object.

class Camera(object):
    def __init__(self, marca, megapixels) -> None:
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} e resolução {self.megapixels} megapixels.')

#ex1 - camera celular
class Camera_cel(Camera):
    def __init__(self, marca, megapixels, quantidade_cameras) -> None:  #basicamente utilizar os atributos da classe PAI e add alguns diferentes;
        super().__init__(marca, megapixels)     #super é uma função indica quais atributos continuam na classe pai.não tendo que repetir métodos anteriormente criados
        self.qtd_cameras = quantidade_cameras
    
    def aplicar_filtro(self, filtro):
        print(f'Aplicando o filtro {filtro}')

    def tirar_foto(self,n_camera):
        print(f'\n Foto tirada com a camera {self.marca} \
e resolução {self.megapixels} megapixels, utilizando a camera numero {n_camera}.')


# Facilmente temos acesso aos metodos e atributos da Classe PAI; > pass
# camera_cel = Camera_cel('Apple','1800')
# print(camera_cel.marca)

#* 01 - Buscando atributos e metodos:
cam_cel = Camera_cel('Sony','25mp',4)
""" print(cam_cel.marca + '\n' + str(cam_cel.qtd_cameras))
cam_cel.aplicar_filtro('B&W')
 """
#* 02 - Modificar o metodo tirar_foto do PAI:
# criei o mesmo metodo tirar foto, porem coloquei mais um argumento Obrigatorio.
cam_cel.tirar_foto(33)

#! Verificar HERANÇA - se uma classe é filho ou não
print(issubclass(Camera_cel,Camera))