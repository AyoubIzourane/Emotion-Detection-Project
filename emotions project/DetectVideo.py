from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout)
import sys

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        print('upload video')
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie", QDir.homePath())

        if fileName != '':
            self.label.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))


        self.label.mediaPlayer.play()


app = QApplication(sys.argv)
videoplayer = VideoPlayer()
videoplayer.resize(640, 480)
videoplayer.show()
sys.exit(app.exec_())