import os
import random
import shutil
import subprocess
from PyQt5.QtCore import QObject, pyqtSignal

class FileManager(QObject):
    def __init__(self):
        super().__init__()
        self.app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.app_dir, "Data")
        self.xnbcli_path = os.path.join(self.data_dir, "App", "xnbcli.exe")
        self.setup_temp_dirs()
        
    def setup_temp_dirs(self):
        os.makedirs(self.data_dir, exist_ok=True)
        rand_str = str(random.randint(1000, 9999))
        self.extract_dir = os.path.join(self.data_dir, f"extract_{rand_str}")
        self.pack_dir = os.path.join(self.data_dir, f"pack_{rand_str}")
        os.makedirs(self.extract_dir, exist_ok=True)
        os.makedirs(self.pack_dir, exist_ok=True)
        
    def cleanup(self):
        shutil.rmtree(self.extract_dir, ignore_errors=True)
        shutil.rmtree(self.pack_dir, ignore_errors=True)
        
    def unpack(self, xnb_path=None):
        if not xnb_path:
            return False
            
        try:
            subprocess.run([self.xnbcli_path, "unpack", xnb_path, self.extract_dir])
            return True
        except Exception as e:
            print(f"Extraction failed: {e}")
            return False
            
    def pack(self, save_as=False, output_path=None):
        if not output_path and not save_as:
            return False
            
        try:
            subprocess.run([self.xnbcli_path, "pack", self.pack_dir, output_path])
            return True
        except Exception as e:
            print(f"Packing failed: {e}")
            return False
