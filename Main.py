
from DirectoriesAndFiles import *
from YoutubeDownload import YoutubeDownload

#Variables de entrada
pathFile = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas"
url = "https://www.youtube.com/watch?v=3j8F-lQUgks&ab_channel=M%C3%A4godeOz"

#comprobacion de rutas de descarga
if existPath(pathFile):
    print("existe")
else:
    print("No existe")
    generatePath()
    print("existe")

#Generacion de instancia    
video = YoutubeDownload(url)

#Acciones a realizar para descargar video
print(video.title)
video.streamAudio()
itagInput = input("inserte el itag")
video.downloadToItag(itag=itagInput,path=pathFile)

#Eliminar instancia del objeto
del video