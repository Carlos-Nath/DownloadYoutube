'''
    * Class:
    * methods:
    * Description: la clase nos sirve para identificar las url de una playlist en youtube
    
    *
'''
#importar libreria a utilizar
from pytube import Playlist

class YoutubePlayList:
    #generar el constructor
    def __init__(self,url):
        self.url = url
        self.playList = Playlist(url)
        self.title = self.playList.title
        self.description = self.playList.description
    
    #obtener la lista de url
    def getListUrl(self):
        print(self.title)
        print(self.description)
        print(self.url)
        return self.playList.video_urls
  