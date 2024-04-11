# packet_sniffing.py
import sys
import time
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
from scapy.all import sniff

# Class for Packet Sniffing Window
class PacketSniffingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        interface_label = QLabel("Enter interface name:")
        layout.addWidget(interface_label)

        self.interface_edit = QLineEdit()
        layout.addWidget(self.interface_edit)

        packet_count_label = QLabel("Enter number of packets to sniff:")
        layout.addWidget(packet_count_label)

        self.packet_count_edit = QLineEdit()
        layout.addWidget(self.packet_count_edit)

        submit_btn = QPushButton("Submit", self)
        submit_btn.clicked.connect(self.start_sniffing)
        layout.addWidget(submit_btn)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)

        self.setLayout(layout)
        self.setWindowTitle('Packet Sniffing')

    def start_sniffing(self):
        iface = self.interface_edit.text()
        try:
            count = int(self.packet_count_edit.text())
            pack = ""
            packets = sniff(count=count, iface=iface)
            for packet in packets:
                pack += str(packet) + "\n"
            self.result_text.setText(pack)
        except Exception as e:
            self.result_text.setText(f"Error: {e}")
