
from DirectoriesAndFiles import *
from Window import *

#comprobacion de rutas de descarga
pathDownloadDefault = joinPath(getCurrentDirectory(),"Deescargas")

if existPath(pathDownloadDefault):
    print("existe")
else:
    print("No existe")
    generatePath(getCurrentDirectory(),"Deescargas")
    print("Se creó")

#importacion de interfaz grafica.
win = Window()
win.mainWindow()
win.setPath(path=pathDownloadDefault)
win.eventWindowMain()
del win