from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

# Load the UI file
window = uic.loadUi("mediaplayerscreen.ui")

# Show the window
window.show()

app.exec()
