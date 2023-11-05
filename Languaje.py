'''
    * Class:
    * methods:
    * Description: la clase nos sirve para contar con un sistema multilenguaje
    
    *para convertir el archivo a ventana es nesesario cambiar la extension de py a pyw
'''
#Clases a utilizar
from DirectoriesAndFiles import *
import json

class Language:
    def __init__(self,directoryName = "Lang",filelanguage = "lang.json"):
        self.lang = directoryName #nombre de la carpeta de lenguajes
        self.fileConfigLang = filelanguage #nombre del archivo de configuracion del lenguaje
        self.currentDirectory = getCurrentDirectory() #Obtiene la carpeta actual
        self.directorylanguage = joinPath(self.currentDirectory,self.lang)
        self.fileDataLang = joinPath(self.directorylanguage,self.fileConfigLang)
        self.jsonLang = json.loads('{}')
    
    def languageFileExist(self):   
        pathExist = existPath(self.directorylanguage)
        if pathExist:
            languageExist = existPath(self.fileDataLang)
            if languageExist == False:
                createlinearFile(self.fileDataLang,'{"Idioma":"spanish.json"}')     
        else:
            generatePath(self.currentDirectory,self.lang)
            createlinearFile(self.fileDataLang,'{"Idioma":"spanish.json"}')
            createlinearFile(joinPath(self.directorylanguage,"spanish.json"),'{"NameTitle":"Descargar Videos","EdchOne": "Descarga Individual","EdchTwo":"Descarga por Playlist","_":"_Default_"}')     
        
    def getDataLang(self):
        languageDataConfig = getlanguageFile(self.fileDataLang)
        languageDataJSONConfig = json.loads(languageDataConfig)
        jsonloadsText = getlanguageFile(self.directorylanguage,languageDataJSONConfig["Idioma"])
        self.jsonLang = json.loads(jsonloadsText)
        del languageDataConfig
        del languageDataJSONConfig
        del jsonloadsText
        
    def getElement(self,element=""):
        elementoTxt = self.jsonLang[element]
        return elementoTxt
    
    def setLanguage(self,newLanguajeFile):
        createlinearFile(self.fileDataLang,'{"Idioma":"'+newLanguajeFile+'"}')        


#iner = Language()
#iner.languageFileExist()
#iner.getDataLang()
#elemento = iner.getElement("_")
#print(elemento)
#iner.setLanguage("spanish.json") #Metodo para cambiar el idioma