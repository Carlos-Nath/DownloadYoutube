from moviepy.editor import *

#variable de entrada
path = "C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas/Mägo de Oz - Pagan Party (Videoclip oficial).mp4"

#-----------------------AUDIO A AUDIO----------------------------

#se carga el fichero en mp4 Audio
firstFile = AudioFileClip(path)

#se cambia la extension del mp4 Audio a mp3
newPath = path.replace(".mp4",".mp3")
print(newPath)

#se convierte a mp3
secondFile = firstFile.write_audiofile(newPath)

#-----------------------VIDEO A AUDIO----------------------------

#se carga el fichero en Video
#firstFile = VideoFileClip(path)
#se convierte a mp3
#secondFile = firstFile.audio.write_audiofile(newPath)