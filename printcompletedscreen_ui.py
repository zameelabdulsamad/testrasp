# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/vokfra/Desktop/pysidetest/printcompletedscreen.ui'
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
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(540, 110, 350, 369))
        self.label_20.setMaximumSize(QtCore.QSize(409, 409))
        self.label_20.setStyleSheet("")
        self.label_20.setLineWidth(0)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/Clip path group.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(720, 510, 231, 119))
        self.frame_5.setMinimumSize(QtCore.QSize(231, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setContentsMargins(-1, -1, 12, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: #939191;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19, 0, QtCore.Qt.AlignRight)
        self.phoneLabel1_4 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.phoneLabel1_4.setFont(font)
        self.phoneLabel1_4.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"\n"
"\n"
"")
        self.phoneLabel1_4.setObjectName("phoneLabel1_4")
        self.verticalLayout_9.addWidget(self.phoneLabel1_4, 0, QtCore.Qt.AlignRight)
        self.mailLabel1_4 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.mailLabel1_4.setFont(font)
        self.mailLabel1_4.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"")
        self.mailLabel1_4.setObjectName("mailLabel1_4")
        self.verticalLayout_9.addWidget(self.mailLabel1_4, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setMaximumSize(QtCore.QSize(30, 30))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("/Users/vokfra/Desktop/pysidetest/../../Downloads/Icon/Outline/chat-alt.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_6.addWidget(self.label_21)
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
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 220, 421, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setEnabled(True)
        self.label_22.setMinimumSize(QtCore.QSize(0, 90))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: #003873;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 600;")
        self.label_22.setLineWidth(0)
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setIndent(0)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: black;\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"line-height: 0.8;\n"
"")
        self.label_23.setLineWidth(0)
        self.label_23.setMidLineWidth(-1)
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setScaledContents(True)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setIndent(0)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_10.addWidget(self.label_23)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel1.setText(_translate("Form", "10:28 AM"))
        self.label_19.setText(_translate("Form", "For support"))
        self.phoneLabel1_4.setText(_translate("Form", "83 3003 1001"))
        self.mailLabel1_4.setText(_translate("Form", "help@kopyfi.com"))
        self.dateLabel1.setText(_translate("Form", "30 June 2023 "))
        self.label_22.setText(_translate("Form", "Print completed"))
        self.label_23.setText(_translate("Form", "<html><head/><body><p>Collect your printout from <span style=\" color:#0253b6;\">Output tray 1</span></p></body></html>"))
