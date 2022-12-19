import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import requests

class FileUploadThread(QThread):
  # Set up a signal to be emitted when the file is uploaded
  uploaded = pyqtSignal()

  def __init__(self, file_path):
    super().__init__()
    self.file_path = file_path

  def run(self):
    # Send a POST request to the server with the file attached
    with open(self.file_path, 'rb') as f:
      files = {'file': f}
      response = requests.post('http://localhost:5000/upload', files=files)
    # Emit the uploaded signal
    self.uploaded.emit()

class FileUploadWidget(QWidget):
  def __init__(self):
    super().__init__()

    # Set up the user interface
    self.file_path_label = QLabel("File path:")
    self.file_path_edit = QLineEdit()
    self.upload_button = QPushButton("Upload")

    self.upload_button.clicked.connect(self.upload_file)

    layout = QVBoxLayout()
    layout.add
