import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[ *** Scanning Target: ' + str(target) + ' *** ]')
    for port in range(1, port_range):
        scan_port(ipaddress=converted_ip, port=port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[!] Open port: " + str(port) + " : " + str(banner.decode().strip('\n')))
        except:
            print("[!] Open port: " + str(port))
    except:
        pass

try:
    targets = str(input("[+] Enter target/s to scan(split multiple targets with ,): "))
    port_range = int(input("[+] Enter amount of ports to scan(starting from 1): "))
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
    print("\n[!] All the scans are completed!\n")
except KeyboardInterrupt:
    print("\n[-] Closing port scanner...\n")
    exit(0)