from __future__ import unicode_literals
import youtube_dl
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle('YouTube mp3 Downloader')
        self.setGeometry(0, 0, 550, 200)

        self.url = ''
        self.get_user()
        self.path = f'C:\\Users\\{self.user}\\Desktop'
        self.UiComponents()


    def UiComponents(self):

        #input URL
        self.line = QLineEdit(self, placeholderText="Insert URL: ")
        self.line.setGeometry(20, 20, 500, 32)

        #path label
        self.label = QLabel(f'{self.path}', self)
        self.label.setGeometry(120,62, 500, 32)

        #choose path button
        self.save_button = QPushButton('Save to: ', self)
        self.save_button.setGeometry(20, 62, 80, 32)
        self.save_button.clicked.connect(self.choose_path)

        #download mp3 button
        self.mp3_button = QPushButton('Download mp3', self)
        self.mp3_button.setGeometry(20, 102, 120, 32)
        self.mp3_button.clicked.connect(self.download_mp3)

        # download mp4 button
        self.mp3_button = QPushButton('Download mp4', self)
        self.mp3_button.setGeometry(150, 102, 120, 32)
        self.mp3_button.clicked.connect(self.download_mp4)

    def get_url(self):
        return self.line.text()


    def format_path_view(self):
        self.path = '\\'.join(self.pre_path.split('/'))


    def choose_path(self):
        self.pre_path = QFileDialog.getExistingDirectory(self)
        self.format_path_view()
        self.display_path()


    def display_path(self):
        self.label.setText(self.path)



    def get_user(self):
        user = os.getlogin()
        self.user = user


    def download_mp3(self):
        try:
            url = self.get_url()
            ydl_opts = {

                'format': 'bestaudio/best',
                'outtmpl': f'{self.path}\\%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]}

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.show_popup()

        except:
            pass

    def download_mp4(self):
        url = self.get_url()
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{self.path}\\%(title)s.%(ext)s',

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Message')
        msg.setText('Download complete !')

        x = msg.exec_()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
