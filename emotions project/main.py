import os

from IPython.external.qt_for_kernel import QtGui
from PyQt5 import QtWidgets, uic
import sys
import cv2 as cv
from PyQt5.QtCore import QSize, QUrl, Qt, QDir
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QLabel, QStyle, QWidget, QPushButton, QSlider, QStatusBar, QHBoxLayout, \
    QVBoxLayout, QMainWindow, QApplication


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view.ui', self)
        self.show()

        self.b1.clicked.connect(self.uploadImage)
        self.b2.clicked.connect(self.uploadVideo)


    def uploadImage(self):
        import DetectImage
        DetectImage.__init__(self)

    def uploadVideo(self):
        import DetectVideo
        DetectVideo.__init__(self)




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
