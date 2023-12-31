# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/vokfra/Desktop/pysidetest/printprogressscreen.ui'
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
        Form.setStyleSheet("background: #FFFFFF;")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(720, 510, 231, 119))
        self.frame_5.setMinimumSize(QtCore.QSize(231, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setContentsMargins(-1, -1, 12, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_17 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: #939191;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_7.addWidget(self.label_17, 0, QtCore.Qt.AlignRight)
        self.phoneLabel1_3 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.phoneLabel1_3.setFont(font)
        self.phoneLabel1_3.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"\n"
"\n"
"")
        self.phoneLabel1_3.setObjectName("phoneLabel1_3")
        self.verticalLayout_7.addWidget(self.phoneLabel1_3, 0, QtCore.Qt.AlignRight)
        self.mailLabel1_3 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.mailLabel1_3.setFont(font)
        self.mailLabel1_3.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"")
        self.mailLabel1_3.setObjectName("mailLabel1_3")
        self.verticalLayout_7.addWidget(self.mailLabel1_3, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.frame_8)
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setMaximumSize(QtCore.QSize(30, 30))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/Icon/Outline/chat-alt.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(204, 360, 551, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setEnabled(True)
        self.label_18.setMinimumSize(QtCore.QSize(0, 90))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: #003873;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 600;")
        self.label_18.setLineWidth(0)
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setIndent(0)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setMaximumSize(QtCore.QSize(521, 12))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 0.745px solid #003873;\n"
"    border-radius: 20.361px;\n"
"    background-color: #E3E3E3;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #003873;\n"
"    border-radius: 20.361px;\n"
"}\n"
"")
        self.progressBar.setProperty("value", 36)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_8.addWidget(self.progressBar)
        self.timeLabel1 = QtWidgets.QLabel(Form)
        self.timeLabel1.setGeometry(QtCore.QRect(20, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.timeLabel1.setFont(font)
        self.timeLabel1.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;")
        self.timeLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel1.setObjectName("timeLabel1")
        self.dateLabel1 = QtWidgets.QLabel(Form)
        self.dateLabel1.setGeometry(QtCore.QRect(760, 20, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.dateLabel1.setFont(font)
        self.dateLabel1.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"text-align: center;\n"
"")
        self.dateLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel1.setObjectName("dateLabel1")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(330, 100, 300, 221))
        self.label_20.setMaximumSize(QtCore.QSize(300, 221))
        self.label_20.setStyleSheet("")
        self.label_20.setLineWidth(0)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/Print Machine.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_17.setText(_translate("Form", "For support"))
        self.phoneLabel1_3.setText(_translate("Form", "83 3003 1001"))
        self.mailLabel1_3.setText(_translate("Form", "help@kopyfi.com"))
        self.label_18.setText(_translate("Form", "Print in progress"))
        self.timeLabel1.setText(_translate("Form", "10:28 AM"))
        self.dateLabel1.setText(_translate("Form", "30 June 2023 "))
