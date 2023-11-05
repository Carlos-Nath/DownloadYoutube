'''
    * Class:
    * methods:
    * Description: la clase nos sirve para descargar los elementos de youtube
    
    *eliminar en prod.
    url = "https://www.youtube.com/watch?v=3j8F-lQUgks&ab_channel=M%C3%A4godeOz"
    path = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas"
'''
#Librerias a utilizar
import pytube

class YoutubeDownload:
    def __init__(self,url):
        self.url = url
        self.youTubeVideo = pytube.YouTube(self.url)
        self.title = self.youTubeVideo.title
        self.lenght = str(self.youTubeVideo.length)
        self.description = str(self.youTubeVideo.description)
        self.metadata = str(self.youTubeVideo._metadata)
        
    #muestra solo los treams de video
    def streamVideo(self):
        listStreams = self.youTubeVideo.streams.filter(only_video=True)
        return listStreams
    
    #muestra solo los treams de musica
    def streamAudio(self):
        listStreams = self.youTubeVideo.streams.filter(only_audio=True)
        return listStreams
            
    #Seleccion de stream por medio de un ITAG    
    def downloadToItag(self,itag,path):
        stream = self.youTubeVideo.streams.get_by_itag(itag)
        stream.download(path)
        