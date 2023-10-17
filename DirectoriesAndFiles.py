'''
    * Class:
    * methods:
    * Description: la clase nos sirve para comprobar si existen las rutas donde se alojará el archivoa descargar
'''
#seccion de librerias a utilizar.
import os

def existPath(Path):
    #Compara si existe la carpeta que ingreso el usuario.    
    isExist = os.path.exists(Path)
    return isExist

def generatePath():
    #Nombre del directoria a crear.
    directory = "Deescargas"
    #Obtener el directorio actual.
    parentDirectory = os.getcwd()
    #Agrupar el directorio en el que se encuentra con el directorio a crear.
    DirectoryComplete = os.path.join(parentDirectory,directory)
    #Crear el directorio completo, la ruta padre con el directorio a crear.
    os.mkdir(DirectoryComplete)
    