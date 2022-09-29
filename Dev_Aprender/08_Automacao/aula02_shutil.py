
#! SHUTIL

""" O módulo shutil oferece várias operações de alto nível em arquivos e coleções de arquivos. 
São fornecidas funções que possuem suporte a cópia e remoção de arquivos. """
import shutil
import os

#copiar um arquivo
""" shutil.copy(src= r'Dev_Aprender\\08_Automacao\\docs\\frutas.txt',
            dst= r'Dev_Aprender\\08_Automacao')
 """
#copiar uma pasta
""" shutil.copytree()

#mover um arquivo ou pasta
shutil.move()

#apagar um arquivo ou pasta
shutil.rmtree()
 """
#compactar
""" shutil.make_archive(base_name = 'docs_backup',format = 'zip',
                    root_dir= r'Dev_Aprender\\08_Automacao\\docs')
#descompactar """
# shutil.unpack_archive()

shutil.move(os.getcwd() + os.sep + 'aula03_csv.py',r'Dev_Aprender\\08_Automacao')