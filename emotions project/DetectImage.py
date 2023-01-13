from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel


def __init__(self):
    print('upload image')
    image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.png *.jpg *.bmp)")
    imagePath = image[0]
    pixmap = QPixmap(imagePath)
    self.label.setPixmap(pixmap)
    self.label.setScaledContents(1)


    # print(ocr.resimden_yaziya(imagePath))
    print(imagePath)