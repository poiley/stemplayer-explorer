from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import pyqtSlot

from mount import get_devices
from stemplayer import stem_player

app = QApplication([])

class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.device_selection()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Stem Player Explorer')
        self.grid = QGridLayout()
        self.setLayout(self.grid)        

    def device_selection(self):
        self.label_devices = QLabel('Devices found:', self)
        self.label_devices.setFont(QFont('Avant Garde', 16))
        
        self.grid.addWidget(self.label_devices, 0, 0)

        DEVICES = get_devices()

        if len(DEVICES) == 1:
            self.device_selected(DEVICES[0])
        else:
            button_row = 1
            for i, device in enumerate(DEVICES):
                device_button = QPushButton('Stem Player [{}]'.format(device.VolumeSerialNumber), self)    
                device_button.clicked.connect(lambda checked, i=i: self.device_selected(DEVICES[i]))
                self.grid.addWidget(device_button, button_row, 1)
                button_row += 1

    def wipe_layout(self):
        for i in reversed(range(self.grid.count())): 
            self.grid.itemAt(i).widget().setParent(None)

    @pyqtSlot()
    def device_selected(self, device):
        self.device = device
        print('Device Selected: {}'.format(self.device))
        self.wipe_layout()
        self.tool()

    def tool(self):
        self.title = QLabel('Device in use: Stem Player [{}]'.format(self.device.VolumeSerialNumber))
        self.title.setFont(QFont('Avant Garde', 16))
        self.grid.addWidget(self.title, 0, 0)
        player = stem_player(self.device)
