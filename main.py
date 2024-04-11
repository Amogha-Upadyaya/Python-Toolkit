# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from ip_domain_analysis import IPDomainWindow
from packet_sniffing import PacketSniffingWindow
from banner_grabbing import BannerGrabbingWindow
from arp_cache_poisoning import ARPCacheDetectionWindow
from wifi_scanner import WiFiScanningWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ip_domain_btn = QPushButton("IP Address Analysis", self)
        ip_domain_btn.clicked.connect(self.ip_domain_window)
        layout.addWidget(ip_domain_btn)

        packet_sniffing_btn = QPushButton("Packet Sniffing", self)
        packet_sniffing_btn.clicked.connect(self.packet_sniffing_window)
        layout.addWidget(packet_sniffing_btn)

        banner_grabbing_btn = QPushButton("Banner Grabbing", self)
        banner_grabbing_btn.clicked.connect(self.banner_grabbing_window)
        layout.addWidget(banner_grabbing_btn)

        arp_cache_detection_btn = QPushButton("ARP Cache Poisoning", self)
        arp_cache_detection_btn.clicked.connect(self.arp_cache_detection_window)
        layout.addWidget(arp_cache_detection_btn)

        wifi_scanning_btn = QPushButton("WiFi Scanner", self)
        wifi_scanning_btn.clicked.connect(self.wifi_scanning_window)
        layout.addWidget(wifi_scanning_btn)

        exit_btn = QPushButton("Exit", self)
        exit_btn.clicked.connect(self.close)
        layout.addWidget(exit_btn)

        self.setLayout(layout)
        self.setWindowTitle('Network Security Toolkit')

    def ip_domain_window(self):
        self.ip_domain_dialog = IPDomainWindow()
        self.ip_domain_dialog.show()

    def packet_sniffing_window(self):
        self.packet_sniffing_dialog = PacketSniffingWindow()
        self.packet_sniffing_dialog.show()

    def banner_grabbing_window(self):
        self.banner_grabbing_dialog = BannerGrabbingWindow()
        self.banner_grabbing_dialog.show()

    def arp_cache_detection_window(self):
        self.arp_cache_detection_dialog = ARPCacheDetectionWindow()
        self.arp_cache_detection_dialog.show()

    def wifi_scanning_window(self):
        self.wifi_scanning_dialog = WiFiScanningWindow()
        self.wifi_scanning_dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
