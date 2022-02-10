
from PyQt5 import QtCore, QtGui, QtWidgets
from multi import Ui_MainWindow
import sys
import datetime
from datetime import*
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
import paho.mqtt.client as mqtt
import json
broker_address="electsut.trueddns.com"
broker_port=27860
client = mqtt.Client("B6215354oangkhana555666") 
client.connect(broker_address,broker_port)
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
import csv

class Project(Ui_MainWindow):
    
    def __init__(self):
        super().setupUi(MainWindow)
        self.gcn()
        self.realtime()
        client.on_message=self.on_message
        client.subscribe("Testinno/b6215354/Test2")
        client.loop_start()
        self.mySum = 0
        self.Sum = 0
        self.sum = 0
        self.Mo = 0
        self.x ='{}'
        self.s = json.loads(self.x)
  

    def gcn(self):
        self.pushButton_4.clicked.connect(self.onclick)
        self.pushButton_3.clicked.connect(self.offclick)
        self.pushButton.clicked.connect(self.Exitclick)


    def onclick(self):
        self.label_9.setText(" MyShop Cha Cha Cha เปิดให้บริการแล้วนะคะ")
        self.s["LED"] = 1
        self.s["state"] = "on"
        self.y=json.dumps(self.s)
        client.publish("Testinno/b6215354/Test3",self.y)
        self.pushButton_4.setStyleSheet ("background-color: rgb(0, 255, 0);")
        self.pushButton_3.setStyleSheet ("background-color: rgb(255, 255, 255);")
        self.label_9.setStyleSheet ("background-color: rgb(170, 255, 255);")
 
    
 

    def offclick(self):
        self.label_9.setText("  กราบขออภัย ร้านปิดให้บริการแล้วค่ะ ")
        self.s["LED"] = 1 
        self.s["state"] = "off"
        self.y = json.dumps(self.s)
        client.publish("Testinno/b6215354/Test3",self.y)
        self.pushButton_4.setStyleSheet ("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setStyleSheet ("background-color: rgb(255, 0, 0);")
        self.label_9.setStyleSheet ("background-color: rgb(255, 85, 127);")
    

    def Exitclick(self):
        sys.exit(0)
    
    def realtime(self):
        self.day = date.today()
        self.label_8.setText(self.day.strftime("%d %B %Y"))
        self.time = datetime.now()
        self.lcdNumber.display(self.time.strftime("%H"))
        self.lcdNumber_5.display(self.time.strftime("%M"))
        self.lcdNumber_6.display(self.time.strftime("%S"))
        

    def on_message(self, client, userdata, message):
        self.myPL = str(message.payload.decode("utf-8"))
        self.mySum = json.loads(self.myPL)
        self.sum = self.mySum["Count = "]
        self.Sum += self.sum
        self.lcdNumber_2.display(self.sum)
        self.lcdNumber_3.display(self.Sum)
        
    
    def CSV(self):
        self.time = datetime.now()
        self.A = self.lcdNumber_2.value()
        self.B = self.lcdNumber_3.value()
        self.plainTextEdit_2.appendPlainText(self.time.strftime,("%s จำนวนคนที่เดินเข้าร้าน = %s ยอดรวมคนที่เข้าร้านวันนี้ = %s" % ( "%c",self.A,self.B )))
        
        with open("ProjectMyshopChaChaCha1.csv","a",newline = "") as f:
            self.DataCSV = csv.write(f)
            self.C = self.time.strftime("%c")
            self.D = ("%s"%self.A)
            self.E = ("%s"%self.B)
            self.DataCSV.writerow([self.C, self.D, self.E])
            print(self.C, self.D, self.E)


if __name__ == "__main__":
    ui =  Project()
    MainWindow.show()
    sys.exit(app.exec_())
