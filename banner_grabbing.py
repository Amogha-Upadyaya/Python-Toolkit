# banner_grabbing.py
import socket
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
import sys

# Function to grab banner
def grab_banner(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target, port))
        banner = s.recv(1024)
        banner_str = banner.decode().strip()
        if "SSH-" in banner_str:
            # This is an SSH banner, return as-is
            return banner_str
        else:
            # Not an SSH banner, return custom error message
            return f"Unexpected banner received - {banner_str}"
    except TimeoutError:
        return "Error: Connection timed out. Please check the target and port."
    except Exception as e:
        return str(e)
    finally:
        s.close()

# Class for Banner Grabbing Window
class BannerGrabbingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        target_label = QLabel("Enter target:")
        layout.addWidget(target_label)

        self.target_edit = QLineEdit()
        layout.addWidget(self.target_edit)

        port_label = QLabel("Enter port:")
        layout.addWidget(port_label)

        self.port_edit = QLineEdit()
        layout.addWidget(self.port_edit)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.grab_banner)
        layout.addWidget(submit_btn)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)

        self.setLayout(layout)
        self.setWindowTitle('Banner Grabbing')

    def grab_banner(self):
        target = self.target_edit.text()
        port = int(self.port_edit.text())
        result = grab_banner(target, port)
        if isinstance(result, str):
            self.result_text.setText(f"Error: {result}")
        else:
            self.result_text.setText(f"Banner from {target}:{port} - {result}")
