from PyQt5.QtWidgets import QApplication , QMainWindow ,QPushButton ,QLabel 
from sys import argv
from PyQt5 import uic
from second import Ui_MainWindow
from pytube import YouTube
import wget
from PyQt5.QtGui import QPixmap
from os import remove
from PySide2extn.RoundProgressBar import roundProgressBar

class FirstWindow(QMainWindow):
    def open_second(self):
        
        self.win=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.win)
        self.ui.label.setText(self.url.text())
        self.lst=[]
        #جلب بيانات الفيديو self.photo.setPixmap(GtGUI.QPixmap("dog.jpg"))
        li=self.url.text()
        link=li.strip()
        yt = YouTube(link)
        #العنوان
        tit=yt.title
        self.ui.title.setText(tit)

        #الصورة
        photo=yt.thumbnail_url
        photo_name=photo.split("/")[-1]
        wget.download(photo)
        pixmap=QPixmap(photo_name)
        self.ui.photo.setPixmap(pixmap.scaled(135,135))
        remove(photo_name)

        
        #الجودات
        #صيغ الفيديو
        vids=yt.streams.filter(progressive=True)
        #وضعها في القائمة
        self.ui.strm.append(vids)
        self.lst.append(vids)

        #صيغ الصوت
        auds=yt.streams.filter(only_audio=True)
        #وضعها في القائمة 
        self.ui.strm.append(auds)
        self.lst.append(auds)
        #ارسال القائمة
        # self.ui.streems=self.lst
        for strm in self.lst:
            self.ui.comboBox.addItem(str(strm))

        
        
        



        self.win.show()
        self.hide()

   

    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui',self)
        self.opsc.clicked.connect(self.open_second)




app=QApplication(argv)
win=FirstWindow()
win.show()
app.exec_()