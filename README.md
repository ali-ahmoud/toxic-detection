# Intrusion Detection System

## Overview
The **Intrusion Detection System (IDS)** is a Python-based security tool designed to detect potential intrusions on both Linux and Windows systems. It provides real-time monitoring of network activity, system processes, file modifications, and logs to identify suspicious behavior. The tool also includes options for network forensics, vulnerability assessments, and attack mitigation.

## Features
- **Detect Unusual Network Connections**: Analyze active network connections for anomalies.
- **Detect Suspicious Processes**: Identify high CPU usage and abnormal processes.
- **Monitor Modified Files**: Detect unauthorized file changes.
- **Analyze System Logs**: Review security-related events.
- **Trace Suspicious Connections**: Perform traceroute analysis on suspicious IPs.
- **Scan Open Ports**: Identify open ports and running services.
- **Vulnerability Assessment**: Test target systems for known vulnerabilities.
- **Exploit Search**: Find known exploits for vulnerabilities using `searchsploit`.
- **Block Attacker IP**: Add firewall rules to block malicious IPs.
- **User-Friendly Interface**: Uses color formatting and an interactive menu for ease of use.

## Installation
### Requirements
Ensure you have the following dependencies installed:
```bash
pip install termcolor
sudo apt install nmap
sudo apt install exploitdb  # For searchsploit
```

### Clone the Repository
```bash
git clone https://github.com/ali-ahmoud/ToxicDetection.git
cd ToxicDetection
```

## Usage
Run the script with:
```bash
python3 toxic_detection.py
```

Follow the interactive menu to perform various security checks.

## Example Output
```
  █████╗ ██╗     ██╗
 ██╔══██╗██║     ██║
 ███████║██║     ██║
 ██╔══██║██║     ██║
 ██║  ██║███████╗██╗
 ╚═╝  ╚═╝╚══════╝╚═╝

  Intrusion Detection System - TOXIC DETECTION
  Author: Ali Mahmoud
  ===========================
  [+] Started at: 2025-03-22 12:34:56

1. Detect Unusual Network Connections
2. Detect Suspicious Processes
3. Detect Modified Files
...
10. Exit

Enter your choice:
```

## Notes
- Run the script with root privileges for full functionality:
  ```bash
  sudo python3 toxic_detection.py
  ```
- Windows users should run the script as Administrator.


## Author
**Ali Mahmoud**


## 📞 Contact
For any inquiries or suggestions, feel free to reach out:
- GitHub: [ali-ahmoud](https://github.com/ali-ahmoud)
- Email: 120180908@fa-hists.edu.eg
