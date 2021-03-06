
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 850)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #eff9fe;\n"
"\n"
"}\n"
" #frame_11{\n"
"    background-color: #2596be;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"#appHeader{\n"
"    color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4 {\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #profileCont, #frame_15{\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"    background-color: #fefeff;\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"}\n"
"#pushButton_3, #pushButton_4{\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.appHeader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.appHeader.setFont(font)
        self.appHeader.setObjectName("appHeader")
        self.horizontalLayout_3.addWidget(self.appHeader)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.headerFrame)
        self.cardsFrame = QtWidgets.QWidget(self.mainBody)
        self.cardsFrame.setMinimumSize(QtCore.QSize(30, 30))
        self.cardsFrame.setSizeIncrement(QtCore.QSize(30, 30))
        self.cardsFrame.setObjectName("cardsFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.cardsFrame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.card1 = QtWidgets.QFrame(self.cardsFrame)
        self.card1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.card1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setMinimumSize(QtCore.QSize(135, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout_2.addWidget(self.frame)
        self.label_4 = QtWidgets.QLabel(self.card1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6.addWidget(self.card1)
        self.card2 = QtWidgets.QFrame(self.cardsFrame)
        self.card2.setMinimumSize(QtCore.QSize(160, 0))
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.card2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setMinimumSize(QtCore.QSize(134, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"font: 75 8pt \"8514oem\";")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_8.addWidget(self.lcdNumber, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_7 = QtWidgets.QLabel(self.card2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6.addWidget(self.card2)
        self.card4 = QtWidgets.QFrame(self.cardsFrame)
        self.card4.setMinimumSize(QtCore.QSize(160, 0))
        self.card4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card4.setObjectName("card4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.card4)
        self.frame_4.setMinimumSize(QtCore.QSize(157, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_13 = QtWidgets.QLabel(self.card4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.horizontalLayout_6.addWidget(self.card4)
        self.verticalLayout.addWidget(self.cardsFrame)
        self.mainFrame = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(160, 0))
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_4 = QtWidgets.QWidget(self.mainFrame)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_9.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_9.addWidget(self.pushButton_3)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(0, 110, 261, 281))
        self.frame_11.setStyleSheet("background-color: rgb(253, 255, 129);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setGeometry(QtCore.QRect(-1, -1, 271, 111))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_2 = QtWidgets.QLabel(self.frame_12)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 129, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.frame_10)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.mainFrame)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.widget_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6, 0, QtCore.Qt.AlignTop)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_7)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_8.addWidget(self.lcdNumber_2)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.widget_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.frame_6 = QtWidgets.QFrame(self.widget_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 40, 111, 41))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(30, 40, 70, 44))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.frame_6)
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.mainFrame)
        self.horizontalLayout.addWidget(self.mainBody)
        self.leftMenu = QtWidgets.QWidget(self.centralwidget)
        self.leftMenu.setMinimumSize(QtCore.QSize(20, 20))
        self.leftMenu.setSizeIncrement(QtCore.QSize(20, 20))
        self.leftMenu.setBaseSize(QtCore.QSize(20, 20))
        self.leftMenu.setStyleSheet("background-color: rgb(121, 233, 255);")
        self.leftMenu.setObjectName("leftMenu")
        self.frame_9 = QtWidgets.QFrame(self.leftMenu)
        self.frame_9.setGeometry(QtCore.QRect(40, 100, 321, 271))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_13 = QtWidgets.QFrame(self.leftMenu)
        self.frame_13.setGeometry(QtCore.QRect(40, 430, 321, 281))
        self.frame_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_13)
        self.spinBox_2.setGeometry(QtCore.QRect(50, 60, 201, 41))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.leftMenu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1225, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appHeader.setText(_translate("MainWindow", "Dashboard"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Date"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.label_11.setText(_translate("MainWindow", "20k"))
        self.label_13.setText(_translate("MainWindow", "?????????????????????????????????????????????????????????????????????????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))
        self.label_2.setText(_translate("MainWindow", "Graph Real Time"))
        self.label_6.setText(_translate("MainWindow", "????????????????????????????????????????????????????????????????????????"))
        self.label_3.setText(_translate("MainWindow", "Graph"))
        self.label_15.setText(_translate("MainWindow", "LED :"))
        self.label.setText(_translate("MainWindow", "????????????????????????????????????????????????????????????????????????????????????????????????"))
        self.label_5.setText(_translate("MainWindow", "Data in CSV"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
