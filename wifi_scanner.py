# wifi_scanner.py
import re
import socket  # Add this line to import the socket module
import scapy.all as scapy
import sys
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit

# Function to scan WiFi networks in a given IP range
def scan_wifi_networks(ip_range):
    try:
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        if ip_add_range_pattern.search(ip_range):
            arp_result = scapy.arping(ip_range, verbose=False)[0]
            for sent, received in arp_result:
                ip = received.psrc
                mac = received.hwsrc
                try:
                    hostname, _, _ = socket.gethostbyaddr(ip)
                except socket.herror:
                    hostname = "Unknown"
                print(f"IP -> {ip}\tMAC -> {mac}\tHostname -> {hostname}")
        else:
            print("Invalid IP address range")
    except Exception as e:
        return str(e)

# Class to redirect stdout to a QTextEdit widget
class StdoutRedirect(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

# Class for WiFi Scanning Window
class WiFiScanningWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ip_range_label = QLabel("Enter IP address range:")
        layout.addWidget(ip_range_label)

        self.ip_range_edit = QLineEdit()
        layout.addWidget(self.ip_range_edit)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.scan_wifi)
        layout.addWidget(submit_btn)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)

        self.setLayout(layout)
        self.setWindowTitle('WiFi Scanning')

        # Redirect stdout to QTextEdit
        sys.stdout = StdoutRedirect()
        sys.stdout.newText.connect(self.append_output)

    # Function to append output to QTextEdit
    def append_output(self, text):
        cursor = self.result_text.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        self.result_text.setTextCursor(cursor)
        self.result_text.ensureCursorVisible()

    # Function to scan WiFi networks
    def scan_wifi(self):
        ip_range = self.ip_range_edit.text()
        result = scan_wifi_networks(ip_range)
        if result:
            self.result_text.setText(f"Error: {result}")
