import pytube
import os
#Descarga de forma directa el video de youtube.
#youTubeVideo = pytube.YouTube("https://youtu.be/44XYEeD1A1U")
#youTubeVideo.streams.first().download("C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube")


#Compara si existe la carpeta de path, si existe, simplemente marca que existe de lo contrario la crea.
isExist = os.path.exists("C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas")
if isExist == True:
    print("Exist")
else:
    print("No Exist")
    #Nombre del directoria a crear.
    directory = "Deescargas"
    #Obtener el directorio actual.
    parentDirectory = os.getcwd()
    #Agrupar el directorio en el que se encuentra con el directorio a crear.
    DirectoryComplete = os.path.join(parentDirectory,directory)
    #Crear el directorio completo, la ruta padre con el directorio a crear.
    os.mkdir(DirectoryComplete)
    
    

#Descarga de elementos por medio de consola.
url = "https://youtu.be/44XYEeD1A1U"
path = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas"


youTubeVideo = pytube.YouTube(url)

#Datos que se pueden obtener del video.
print("Title........." + youTubeVideo.title)
print("lenght......." + str(youTubeVideo.length))
print("Description..." + str(youTubeVideo.description))
print("Metadata....." + str(youTubeVideo._metadata))

#muestra solo los treams de video
listStreams = youTubeVideo.streams.filter(only_video=True).all()
for streams in listStreams:
    print (streams)

#muestra solo los treams de musica
listStreams = youTubeVideo.streams.filter(only_audio=True).all()
for streams in listStreams:
    print (streams)

#Seleccion de stream por medio de un ITAG
ElemenToDownload = "139" #número del itag "estream"
stream = youTubeVideo.streams.get_by_itag(ElemenToDownload)
#stream.download(path)
