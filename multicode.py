
from PyQt5 import QtCore, QtGui, QtWidgets
from multi import Ui_MainWindow
import sys
from datetime import*
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
import paho.mqtt.client as mqtt
import json
broker_address="electsut.trueddns.com"
broker_port=27860
client = mqtt.Client("B6215354oangkhana123456")  #ถ้าค่าไม่มาหรือไฟไม่ติดให้ลองเปลี่ยนmqtt.clineดู
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
        client.on_message = self.on_message
        client.subscribe("Testinno/b6215354/Test2")
        client.loop_start()
        self.mySum = 0
        self.Sum = 0
        self.sum = 0
        self.STOP = 0
        self.x ='{}'
        self.s = json.loads(self.x)
        self.pntick = QtCore.QTimer()
        self.pntick.timeout.connect(self.realtime)
        self.pntick.start(1500)

        self.mygrap=pg.PlotWidget(self.widget_3) 
        self.mygrap.setGeometry(QtCore.QRect(10,20,300,180)) 
        self.mygrap.setObjectName("grapgview")
        self.dataline=self.mygrap.plot() 


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
        self.lcdNumber_2.setStyleSheet ("background-color: rgb(170, 255, 165);")
        self.lcdNumber_3.setStyleSheet ("background-color: rgb(170, 255, 165);")
        self.pntick.timeout.connect(self.CSV)
        self.pntick.start(2000)

    def offclick(self):
        self.label_9.setText("  กราบขออภัย ร้านปิดให้บริการแล้วค่ะ ")
        self.s["LED"] = 1 
        self.s["state"] = "off"
        self.y = json.dumps(self.s)
        client.publish("Testinno/b6215354/Test3",self.y)
        self.pushButton_4.setStyleSheet ("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setStyleSheet ("background-color: rgb(255, 0, 0);")
        self.label_9.setStyleSheet ("background-color: rgb(255, 85, 127);")   
        self.lcdNumber_2.setStyleSheet ("background-color: rgb(255, 85, 127);")
        self.lcdNumber_3.setStyleSheet ("background-color: rgb(255, 85, 127);")
        self.pntick.stop()

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
        #print(self.myPL)
        self.mySum = json.loads(self.myPL)
        self.sum = self.mySum["Count = "]
        self.Sum += self.sum
        self.lcdNumber_2.display(self.sum)
        self.lcdNumber_3.display(self.Sum)

        
    def CSV(self):    
        self.time = datetime.now()
        self.A = self.lcdNumber_2.value()
        self.B = self.lcdNumber_3.value()
        self.plainTextEdit_4.appendPlainText(self.time.strftime("%s จำนวนคนที่เดินเข้าร้าน = %s ยอดรวมคนที่เข้าร้านวันนี้ = %s" % ( "%c",self.A,self.B )))
        
        with open("ProjectFinishofCSV.csv","a",newline ="") as f:
            self.DataCSV = csv.writer(f)
            self.C = self.time.strftime("%c")
            self.D = ("%s"%self.A)
            self.E = ("%s"%self.B)
            self.DataCSV.writerow([self.C, self.D, self.E])

    def udplot(self):
        self.x=np.arange(self.lcdNumber_2.value()) 
        self.y=np.sin(self.x) 
        self.dataline.setData(self.x,self.y)
   
 

if __name__ == "__main__":
    ui =  Project()
    ui.udplot()
    MainWindow.show()
    sys.exit(app.exec_())
    
    
