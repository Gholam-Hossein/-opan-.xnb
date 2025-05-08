from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox

class ControlPanel(QWidget):
    def __init__(self, file_manager):
        super().__init__()
        self.file_manager = file_manager
        self.init_ui()
        
    def init_ui(self):
        layout = QHBoxLayout()
        
        self.unpack_btn = QPushButton("Extract")
        self.pack_btn = QPushButton("Pack")
        self.pack_as_btn = QPushButton("Pack As")
        
        self.extract_options = QComboBox()
        self.extract_options.addItems(["Flat", "With Folder"])
        
        layout.addWidget(self.unpack_btn)
        layout.addWidget(self.extract_options)
        layout.addWidget(self.pack_btn)
        layout.addWidget(self.pack_as_btn)
        
        self.setLayout(layout)
        self.connect_signals()
        
    def connect_signals(self):
        self.unpack_btn.clicked.connect(self.file_manager.unpack)
        self.pack_btn.clicked.connect(lambda: self.file_manager.pack(False))
        self.pack_as_btn.clicked.connect(lambda: self.file_manager.pack(True))
