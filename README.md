# Python Toolkit

## Description
Developed a comprehensive toolkit for network security analysis and monitoring, incorporating various Python scripts and tools like Scapy, socket, etc. The toolkit includes modules for IP Address and Domain Analysis, Packet Sniffing, Banner Grabbing, ARP Cache Poisoning, and Wi-Fi Scanning.

## Created by:
Amogha Upadyaya

## Libraries and dependencies required for the Python Toolkit project.
pyqt5==5.15.6   # PyQt5 GUI framework

scapy==2.4.5    # Scapy network protocol library

## Installation Instructions
To install and set up the project, follow these steps:
1. Install Python on your system if not already installed.
2. Clone the repository to your local machine using `git clone https://github.com/your-username/your-repository.git`.
3. Navigate to the project directory.
4. Install the required dependencies using `pip install -r requirements.txt`.

## Usage
To use the project, follow these steps:
1. Run the `main.py` script using Python.
2. Select the desired functionality from the available options in the GUI interface.
3. Follow the on-screen instructions to perform the selected network security analysis tasks.

## Contributing
Contributions to the project are welcome! If you'd like to contribute, please follow these guidelines:
- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and test thoroughly.
- Submit a pull request detailing your changes, including a clear description of the problem and solution.

## Credits
- [Scapy](https://scapy.net/) - A powerful interactive packet manipulation program.
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) - A set of Python bindings for the Qt application framework.
- A special thanks to my mentor, Mr. Mir Junaid Rasool, for his guidance in the completion of the project. I also thank the contributors and developers of the libraries used in this toolkit.

## Additional Documentation
For more detailed documentation and resources, please refer to the [Wiki](https://github.com/your-username/your-repository/wiki) section of the project repository.

## Brief Description of Code/Program Files
1. `main.py`: Python script for the main application interface using PyQt5 to provide a GUI for selecting various network security analysis tasks.
2. `ip_domain_analysis.py`: Python script for IP Domain Analysis, including functions to retrieve IP address from domain names.
3. `packet_sniffing.py`: Python script for Packet Sniffing, utilizing Scapy for sniffing network packets.
4. `banner_grabbing.py`: Python script for Banner Grabbing, implementing socket programming to retrieve banners from target hosts.
5. `arp_cache_poisoning.py`: Python script for ARP Cache Poisoning Detection, employing Scapy for sending spoofed ARP packets.
6. `wifi_scanner.py`: Python script for WiFi Scanning, using Scapy to scan WiFi networks in a given IP range.
