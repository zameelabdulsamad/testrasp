import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Remove window frame and set full screen
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()

        uic.loadUi('secondpage.ui', self)