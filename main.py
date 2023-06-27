from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import sys

app = QApplication([])

window = QWidget()

# Set window attributes
window.setWindowFlag(Qt.CustomizeWindowHint, True)
window.setWindowFlag(Qt.FramelessWindowHint, True)
window.showFullScreen()

# Set window background color
palette = window.palette()
palette.setColor(QPalette.Window, QColor(0, 0, 255))
window.setPalette(palette)

# Create a label with bold text
label = QLabel("KOPYFI")
font = QFont()
font.setBold(True)
label.setFont(font)

# Set the label alignment to center
label.setAlignment(Qt.AlignCenter)

# Create a loading indicator (progress bar)
loading = QProgressBar()
loading.setRange(0, 0)
loading.setStyleSheet(
    "QProgressBar {border: none; background-color: transparent;} QProgressBar::chunk {background-color: white;}"
)

# Create a layout and add the label and loading indicator to it
layout = QVBoxLayout(window)
layout.addWidget(label)
layout.addWidget(loading)

window.show()

sys.exit(app.exec_())
