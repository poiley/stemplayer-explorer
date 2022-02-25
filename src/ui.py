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
    
    def wipe_layout(self):
        for i in reversed(range(self.grid.count())): 
            self.grid.itemAt(i).widget().setParent(None)
    
    def initUI(self):
        self.setGeometry(500, 500, 600, 500)
        self.setWindowTitle('Stem Player Explorer')
        self.grid = QGridLayout()
        self.setLayout(self.grid)        

    def device_selection(self):
        self.label_devices = QLabel('Devices found:', self)
        self.label_devices.setFont(QFont('Avant Garde', 16))
        
        self.grid.addWidget(self.label_devices, 0, 0)

        DEVICES = get_devices()
        if not DEVICES:
            self.label_devices.setText('No Device Found')
        elif len(DEVICES) == 1:
            self.device_selected(DEVICES[0])
        else:
            button_row = 1
            for i, device in enumerate(DEVICES):
                device_button = QPushButton('Stem Player [{}]'.format(self.device), self)    
                device_button.clicked.connect(lambda checked, i=i: self.device_selected(DEVICES[i]))
                self.grid.addWidget(device_button, button_row, 1)
                button_row += 1

    def tool(self):
        self.player = stem_player(self.device)

        self.title = QLabel('Device in use: Stem Player [{}]'.format(self.player), self)
        self.title.setFont(QFont('Avant Garde', 15))
        self.grid.addWidget(self.title, 0, 0)
        
        self.album_grid = QGridLayout()
        row = 0
        for i, album in enumerate(self.player.library.albums):
            album_item = QRadioButton(album.metadata['title'], self)
            album_item.toggled.connect(lambda checked, i=i: self.album_selected(self.player.library.albums[i].dir))
            self.album_grid.addWidget(album_item, row, 0)
            row += 1

        self.left_column = QGridLayout()
        self.left_column.addLayout(self.album_grid, 0, 0)
        
        self.grid.addLayout(self.left_column, 1, 0)

        self.album_info = QLabel('', self)
        self.album_info.setWordWrap(True)
        self.album_info.setFixedWidth(300)
        self.album_info.setMargin(25)
        self.album_info.setFont(QFont('Avant Garde', 12))

        self.track_info = QLabel('', self)
        self.track_info.setWordWrap(True)
        self.track_info.setFixedWidth(300)
        self.track_info.setFont(QFont('Avant Garde', 12))

        self.left_column.addWidget(self.album_info, 1, 0)
        self.grid.addWidget(self.track_info, 1, 1)
    
    @pyqtSlot()
    def device_selected(self, device):
        self.device = device
        self.wipe_layout()
        self.tool()

    @pyqtSlot()
    def album_selected(self, album):
        album_obj = self.player.library.get_album(album)
        tracks_obj = album_obj.tracks
        track_info_text = ''
        for track in tracks_obj:
            track_info_text += ' - {}\n'.format(track.metadata['metadata']['title'])
        
        album_info_str = ''
        for metadata_object_key in album_obj.metadata:
            album_info_str += '{}\t{}\n'.format(
                metadata_object_key.capitalize(), 
                album_obj.metadata[metadata_object_key] )
        
        self.album_info.setText(album_info_str)
        self.track_info.setText(track_info_text)