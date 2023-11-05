from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip

class TransformExtension:
        
    #Se transforma de Audio a Audio
    def changeFileAudioAudio(Self,pathFile):
        #se carga el fichero en mp4 Audio
        fileToChange = AudioFileClip(pathFile)
        #se cambia la extension del mp4 Audio a mp3
        newPath = pathFile.replace(".mp4",".mp3")
        print(newPath)
        #se convierte a mp3
        fileToChange.write_audiofile(newPath)
    
    #Se transforma de Video a Audio            
    def changeFileVideoAudio(Self,pathFile):
        #se carga el fichero en Video
        firstFile = VideoFileClip(pathFile)
        #se cambia la extension del mp4 Audio a mp3
        newPath = pathFile.replace(".mp4",".mp3")
        print(newPath)
        #se convierte a mp3
        firstFile.audio.write_audiofile(newPath)
        remove(pathFile)

'''        
#variable de entrada
tf = TransformExtension()
tf.changeFileAudioAudio("C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas/La Costa Del Silencio.mp4")
del tf
'''