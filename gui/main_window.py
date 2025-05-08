from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.file_view import FileView
from gui.controls import ControlPanel
from core.file_manager import FileManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XNB Manager")
        self.resize(800, 600)
        
        self.file_manager = FileManager()
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.control_panel = ControlPanel(self.file_manager)
        self.file_view = FileView(self.file_manager)
        
        layout.addWidget(self.control_panel)
        layout.addWidget(self.file_view)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
