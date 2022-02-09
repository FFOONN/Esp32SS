
from PyQt5 import QtCore, QtGui, QtWidgets
from kk import Ui_MainWindow
import sys

from datetime import*





app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
import paho.mqtt.client as mqtt
import json
broker_address="electsut.trueddns.com"
broker_port=27860
client = mqtt.Client("B6215354oangkhana555")  #ถ้าไฟไม่ติดให้เปลี่ยนclient
client.connect(broker_address,broker_port)



class mggh(Ui_MainWindow):
    
    def __init__(self):
        super().setupUi(MainWindow)
        self.gcn()
        self.realtime()
       
 

    def gcn(self):
        self.pushButton_4.clicked.connect(self.onclick)
        self.pushButton_3.clicked.connect(self.offclick)
    def onclick(self):
        print("Start")
    def offclick(self):
        print("Stop")

    def realtime(self):
        self.day = date.today()
        self.label_8.setText(self.day.strftime("%d %B %Y"))
        self.time = datetime.now()
        self.lcdNumber.display(self.time.strftime("%H:%M"))
     


if __name__ == "__main__":
    ui = mggh()
    MainWindow.show()
    sys.exit(app.exec_())
