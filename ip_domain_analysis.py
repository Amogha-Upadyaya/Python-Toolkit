# ip_domain_analysis.py
import socket
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject
import sys

# Function to get the IP address of a domain
def get_domain_ip(name, tld):
    try:
        full_address = f"www.{name}.{tld}"
        ip_address = socket.gethostbyname(full_address)
        return full_address, ip_address
    except Exception as e:
        return str(e)

# Class for IP Domain Analysis Window
class IPDomainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        domain_name_label = QLabel("Enter domain name:")
        layout.addWidget(domain_name_label)

        self.domain_name_edit = QLineEdit()
        layout.addWidget(self.domain_name_edit)

        tld_label = QLabel("Enter top level domain:")
        layout.addWidget(tld_label)

        self.tld_edit = QLineEdit()
        layout.addWidget(self.tld_edit)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.analyze_domain)
        layout.addWidget(submit_btn)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)

        self.setLayout(layout)
        self.setWindowTitle('IP Domain Analysis')

    def analyze_domain(self):
        domain_name = self.domain_name_edit.text()
        tld = self.tld_edit.text()
        result = get_domain_ip(domain_name, tld)
        if isinstance(result, tuple):
            full_address, ip_address = result
            self.result_text.setText(f"Your URL is -> {full_address}\nYour IP Address is -> {ip_address}")
        else:
            self.result_text.setText(f"Error: {result}")

# Class to redirect stdout to a QTextEdit widget
class StdoutRedirect(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))
