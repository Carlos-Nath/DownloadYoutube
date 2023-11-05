'''
    * Class:
    * methods:
    * Description: la clase nos sirve para comprobar si existen las rutas donde se alojará el archivoa descargar
'''
#seccion de librerias a utilizar.
import os

def getCurrentDirectory():
    currentDirectory = os.getcwd()
    return currentDirectory
def existPath(Path):
    #Compara si existe la carpeta que ingreso el usuario.    
    isExist = os.path.exists(Path)
    return isExist
def joinPath(firstPath = "", secondPath = ""):
    pathJoin = os.path.join(firstPath,secondPath)
    return pathJoin
def generatePath(parentDirectory = "",directory = ""):
    DirectoryComplete = joinPath(parentDirectory,directory)
    #Crear el directorio completo, la ruta padre con el directorio a crear.
    os.mkdir(DirectoryComplete)
def createlinearFile(filepath = "",text = ""):
    file = open(filepath,"w",encoding="utf-8")
    file.write(text)
    file.close()
#Eliminar Archivos
def deleteFile(pathFile):
    os.remove(pathFile)
    
#Leer datos de archivo de lenguaje principal
def getlanguageFile(path = "",languageSelected = ""):
    #path = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/lang/lang.json"
    #path = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/lang/"
    #languageSelected = "english.json"
    if languageSelected == "":
        archivo = open(path)
    else:
        archivo = open(joinPath(path,languageSelected),encoding="utf-8")
    text = archivo.read()
    archivo.close()
    return text

