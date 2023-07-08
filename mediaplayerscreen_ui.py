# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/vokfra/Desktop/pysidetest/mediaplayerscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 640)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 640))
        self.frame.setStyleSheet("background: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.qrFrame1 = QtWidgets.QFrame(self.frame)
        self.qrFrame1.setGeometry(QtCore.QRect(800, 380, 161, 168))
        self.qrFrame1.setMinimumSize(QtCore.QSize(0, 0))
        self.qrFrame1.setStyleSheet("background-color: white;\n"
"border: 1px solid white;\n"
"border-bottom-left-radius: 20px;\n"
"border-top-left-radius: 20px;\n"
"width: 178.333px;\n"
"height: 168.333px;")
        self.qrFrame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qrFrame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qrFrame1.setObjectName("qrFrame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.qrFrame1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.qrFrame1)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-weight: 600;\n"
"\n"
"\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame_3 = QtWidgets.QFrame(self.qrFrame1)
        self.frame_3.setStyleSheet("    background-color: white;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(91, 91))
        self.label_2.setStyleSheet("width: 91.528px;\n"
"height: 91.528px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/dummyQRCode.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setMaximumSize(QtCore.QSize(10, 20))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/Icon.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout_2.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Scan QR CODE"))