'''
    * Class:
    * methods:
    * Description: la clase nos sirve para generar ventanas graficas por medio de tkinter
    
    *para convertir el archivo a ventana es nesesario cambiar la extension de py a pyw
'''
#librerias a utilizar
import pyperclip as Clipboard
from Languaje import *
from tkinter import Tk
from tkinter import ttk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Listbox
from tkinter import StringVar
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import Menubutton
from tkinter import END as End
from YoutubeDownload import YoutubeDownload
from TransformExtension import TransformExtension

class Window:
    def __init__(Self):
        Self.lang = Language(directoryName = "Lang",filelanguage = "Lang.json")
        Self.lang.languageFileExist()
        Self.lang.getDataLang()
        Self.listItags = []
        Self.addListItems = True
        Self.PathDownload = ""
                     
    def mainWindow(Self):
        #Se genera la ventana
        Self.window = Tk()
        Self.window.title(Self.lang.getElement("NameTitle"))
        Self.window.resizable(False,False)
        Self.stringURLLab = StringVar(value='t')
        #Se Genera el menú
        Self.insertMainMenu()
        #Se genera el frame con pestañas
        Self.notebook = ttk.Notebook(Self.window)
        Self.notebook.pack(fill="both",expand="yes")
        Self.notebook.config(width="350",height="350")
        #se agrega pestañas
        Self.eachOne = ttk.Frame(Self.notebook)
        Self.notebook.add(Self.eachOne,text=Self.lang.getElement("EdchOne"))
        Self.insertEachOneElemensts()
        #Se agrega la segunda pestaña
        '''
        eachTwo = ttk.Frame(Self.notebook)
        Self.notebook.add(eachTwo,text=Self.lang.getElement("EdchTwo"))
        '''
       
    def eventWindowMain(Self):
        #Se mantiene la escucha de la ventana
        Self.window.mainloop()    
        
    def insertMainMenu(Self):
        Self.mainFrame = Frame(Self.window,bg="gray")
        Self.mainFrame.pack(fill="x",side="top")
        
        archivo = Menubutton(Self.mainFrame,text="Archivo",foreground="black")
        archivo.pack(side="left")
        
    def insertEachOneElemensts(Self):
        Label(Self.eachOne,text=Self.lang.getElement("MainLabel")).pack()
        
        Self.labelURL = Label(Self.eachOne,text=Self.lang.getElement("InputURL"))
        Self.labelURL.pack()
        Self.labelURL.place(x="20",y="25")
        
        Self.buttonPasteURL = Button(Self.eachOne,text=Self.lang.getElement("PasteURL"),command=lambda: Self.pasteURL())
        Self.buttonPasteURL.pack()
        Self.buttonPasteURL.place(x="265",y="25")
        
        Self.textUrl = Entry(Self.eachOne,width="50")
        Self.textUrl.pack()
        Self.textUrl.place(x="23",y="55")
        
        Self.selecItag = Label(Self.eachOne,text=Self.lang.getElement("SelectItag"))
        Self.selecItag.pack()
        Self.selecItag.place(x="20",y="80")
        
        Self.listBoxItags = Listbox(Self.eachOne, width="50",height="9")
        Self.listBoxItags.config(yscrollcommand=lambda: Self.scrollbarItagsVer.set())
        Self.listBoxItags.place(x="23",y="100")
        
        Self.scrollbarItagsVer = Scrollbar(Self.listBoxItags, orient="vertical",command=Self.listBoxItags.yview)
        Self.scrollbarItagsVer.place(x=285,y=0,height=145)
        
        Self.scrollbarItagsHor = Scrollbar(Self.listBoxItags, orient="horizontal",command=Self.listBoxItags.xview)
        Self.scrollbarItagsHor.place(x=0,y=128,width=287)
                
        Self.textPathLabel = Label(Self.eachOne,text=Self.lang.getElement("PathStr"))
        Self.textPathLabel.pack()
        Self.textPathLabel.place(x="20",y="250")
        
        Self.textPathStr = Label(Self.eachOne,textvariable=Self.stringURLLab,width="31",bg="#e9e9e9")
        Self.textPathStr.pack()
        Self.textPathStr.place(x="23",y="272")
        
        Self.buttonDownload = Button(Self.eachOne,text=Self.lang.getElement("ChangePath"),command=lambda: Self.changePath())
        Self.buttonDownload.pack()
        Self.buttonDownload.place(x="245",y="270")
        
        Self.buttonDownload = Button(Self.eachOne,text=Self.lang.getElement("ButtonDowload"),command=lambda: Self.downloadSingle())
        Self.buttonDownload.pack()
        Self.buttonDownload.place(x="265",y="310")
    
    def pasteURL(Self):
        Self.textUrl.delete(0,End)
        Self.textUrl.insert(0,Clipboard.paste())
        Self.getVideoStream(Clipboard.paste())
        
    def getVideoStream(Self,url):
        DatosListItags = []
        Self.video = YoutubeDownload(url)
        listItags = Self.video.streamAudio()
        for listas in listItags:
            DatoListItag = str(listas).replace("<Stream: "," ").replace(">"," ")               
            DatosListItags.append(DatoListItag)
        Self.setItemsTag(DatosListItags)
        
    def changePath(Self):
        print("m")

    def setItemsTag(Self,list = []):    
        if Self.addListItems:
            Self.listItags = list
            for index,tagItem in enumerate(list):
                Self.listBoxItags.insert(index,tagItem)
            Self.listBoxItags.update()
            Self.addListItems = False
    #
    #            
    def SelectedItem(Self):
        for item in Self.listBoxItags.curselection():
            selectedItem = Self.listBoxItags.get(item)
            print(selectedItem)
            listDataItag = str(selectedItem).split()
            itag = listDataItag[0].replace("itag="," ").replace('"',' ').strip()
            extension = listDataItag[1].replace('mime_type="audio/',' ').replace('"',' ').strip()
            
            #print(itag)
            Self.video.downloadToItag(itag,Self.PathDownload)
            #Transfprmar de audio a audio
            Self.transformExtension = TransformExtension()
            Self.transformExtension.changeFileAudioAudio(joinPath(Self.PathDownload,Self.video.title+"."+extension))
            #Eliminar archivo
            deleteFile(joinPath(Self.PathDownload,Self.video.title+"."+extension))
            
               
    def downloadSingle(Self):
        Self.SelectedItem()
        Self.addListItems = True
        
    def setPath(Self,path):
        if path == "":
            messagebox.showerror(message="No se puede descargar debido a que no hay una ruta de descarga valida",title="Error en ruta")
        else:
            Self.PathDownload = path
            labelPath = "..."+path[-33:]
            Self.stringURLLab.set(value=labelPath)
            #print(Self.stringURL.get())
            
'''
if __name__ == '__main__':
    ini = Window()
    ini.mainWindow()
    ini.setPath(path="C:/Users/NATH_VAIO/Documents/Python/DownloadYoutube/Deescargas")
    ini.eventWindowMain()
    del ini
       '''