import os
import platform
import subprocess
import time
from datetime import datetime
from termcolor import colored

def banner():
    banner = """
  █████╗ ██╗     ██╗
 ██╔══██╗██║     ██║
 ███████║██║     ██║
 ██╔══██║██║     ██║
 ██║  ██║███████╗██╗
 ╚═╝  ╚═╝╚══════╝╚═╝
       """
    for line in banner.split('\n'):
        print(colored(line, 'cyan'))
        time.sleep(0.2)
    print(colored("\tIntrusion Detection System - TOXIC-DETECTION", 'yellow', attrs=['bold']))
    print(colored("\tAuthor: Ali Mahmoud", 'yellow', attrs=['bold']))
    print(colored(f"\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 'green'))
    print("\n" + "="*50 + "\n")


 

    print(colored(f"[+] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n", "yellow"))
    
    # Display system-specific notice
    if platform.system() == "Windows":
        print(colored("[!] Note: Some features require Administrator privileges and certain tools like 'nmap' or 'searchsploit' may not be installed by default on Windows.", "red"))
    else:
        print(colored("[+] Running on Linux. Most features should work without additional setup.", "green"))

def detect_unusual_connections():
    print(colored("[+] Checking for unusual network connections...", "blue"))
    command = "netstat -ano" if platform.system() == "Windows" else "netstat -tunapl"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def detect_suspicious_processes():
    print(colored("[+] Checking for suspicious processes...", "blue"))
    command = "tasklist" if platform.system() == "Windows" else "ps aux --sort=-%cpu"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def detect_modified_files(directory="/etc" if platform.system() != "Windows" else "C:\\Windows"):
    print(colored(f"[+] Checking for modified files in {directory}...", "blue"))
    command = f"find {directory} -type f -mtime -1" if platform.system() != "Windows" else "forfiles /P C:\\Windows /D -1"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def analyze_logs():
    print(colored("[+] Analyzing system logs...", "blue"))
    command = "wevtutil qe Security /c:10 /rd:true /f:text" if platform.system() == "Windows" else "grep 'Failed password' /var/log/auth.log | tail -n 10"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def trace_source(ip):
    print(colored(f"[+] Tracing source of IP: {ip}...", "blue"))
    command = f"traceroute {ip}" if platform.system() != "Windows" else f"tracert {ip}"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def scan_open_ports(ip):
    print(colored(f"[+] Scanning open ports on {ip}...", "blue"))
    command = f"nmap -sV -Pn {ip}"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def block_attacker(ip):
    print(colored(f"[+] Blocking attacker IP: {ip}...", "red"))
    command = f"sudo iptables -A INPUT -s {ip} -j DROP" if platform.system() != "Windows" else f"netsh advfirewall firewall add rule name='Block {ip}' dir=in action=block remoteip={ip}"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def exploit_vulnerability(ip):
    print(colored(f"[+] Testing for vulnerabilities on {ip}...", "blue"))
    command = f"nmap --script=vuln {ip}"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def search_exploit(ip):
    print(colored(f"[+] Searching for exploits related to {ip}...", "blue"))
    command = f"searchsploit {ip}"
    result = subprocess.getoutput(command)
    print(colored(result, "green"))

def main():
    banner()
    try:
        while True:
            print(colored("\n1. Detect Unusual Network Connections", "yellow"))
            print(colored("2. Detect Suspicious Processes", "yellow"))
            print(colored("3. Detect Modified Files", "yellow"))
            print(colored("4. Analyze Logs", "yellow"))
            print(colored("5. Trace Source of Suspicious Connection", "yellow"))
            print(colored("6. Scan Open Ports of an IP", "yellow"))
            print(colored("7. Test for Vulnerabilities", "yellow"))
            print(colored("8. Search for Exploits", "yellow"))
            print(colored("9. Block Attacker IP", "yellow"))
            print(colored("10. Exit", "red"))
            
            choice = input(colored("\nEnter your choice: ", "cyan"))
            
            if choice == "1":
                detect_unusual_connections()
            elif choice == "2":
                detect_suspicious_processes()
            elif choice == "3":
                detect_modified_files()
            elif choice == "4":
                analyze_logs()
            elif choice == "5":
                ip = input(colored("Enter the suspicious IP: ", "cyan"))
                trace_source(ip)
            elif choice == "6":
                ip = input(colored("Enter the IP to scan for open ports: ", "cyan"))
                scan_open_ports(ip)
            elif choice == "7":
                ip = input(colored("Enter the IP to test for vulnerabilities: ", "cyan"))
                exploit_vulnerability(ip)
            elif choice == "8":
                ip = input(colored("Enter the search term for exploits: ", "cyan"))
                search_exploit(ip)
            elif choice == "9":
                ip = input(colored("Enter the attacker IP to block: ", "cyan"))
                block_attacker(ip)
            elif choice == "10":
                print(colored("[+] Exiting...", "red"))
                break
            else:
                print(colored("[!] Invalid choice, please try again.", "red"))
            
            time.sleep(2)
    except KeyboardInterrupt:
        print(colored("\n[!] Exiting due to user interruption...", "red"))
        exit()

if __name__ == "__main__":
    main()
