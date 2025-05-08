from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QFileSystemModel

class FileView(QTreeView):
    def __init__(self, file_manager):
        super().__init__()
        self.file_manager = file_manager
        self.setup_model()
        
    def setup_model(self):
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
        self.setModel(self.model)
        self.setRootIndex(self.model.index(self.file_manager.extract_dir))
