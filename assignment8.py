# assignment 8 by Aman and Vikas

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import time

from assignment8_gui import assignment8_ui

import pyvisa

rm = pyvisa.ResourceManager()
rm.list_resources()
# ('ASRL1::INSTR', 'ASRL3::INSTR', 'ASRL4::INSTR')

rasberry = 'ASRL4::INSTR'
pico = rm.open_resource(rasberry)

def data_source():
    t = x = time.time() 
    y = pico.query('MEAS:VOLT?')
    return x,y

class data_acquisition_thread(QThread):

    new_value = pyqtSignal(list)
    
    def run(self):
        while True:
            x, y = data_source()
            self.new_value.emit([x,y])
            time.sleep(1)

class assignment8(QMainWindow):    
                 
    
    def __init__(self):         

        super().__init__()       
        self.ui = assignment8_ui()                          
        self.ui.setupUi(self)   

        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.ui.graph.addWidget(self.canvas)                           
        
        self.ui.pb_start.clicked.connect(self.start)
        self.ui.pb_stop.clicked.connect(self.stop)

        self.t = []
        self.y = []  

        pico.write('How:are:you?')
        print(pico.read())

       
    def start(self):
        self.ui.pb_start.setEnabled(False)
        self.ui.pb_stop.setEnabled(True)
        
        self.canvas.axes.clear() #clear not working if I start after stopping
       # self.canvas.draw()

        self.counter = data_acquisition_thread()
        self.counter.new_value.connect(self.showmap)
        self.counter.start()
        print("Started.\n")

    def showmap(self,data):
        
        self.t.append(data[0])
        self.y.append(data[1])
        self.canvas.axes.plot(self.t,self.y,c='blue')
        self.canvas.axes.set_xlabel('time')
        self.canvas.axes.set_ylabel('voltage')
        self.canvas.draw()

    def stop(self):
        self.counter.terminate()
    
        self.ui.pb_start.setEnabled(True)
        self.ui.pb_stop.setEnabled(False)
        print("Stopped.")

app = QApplication([])
window = assignment8()
window.show()
app.exec_()