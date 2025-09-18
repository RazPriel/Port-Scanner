# Port-Scanner
A lightweight Python-based port scanner that checks for open ports and grabs service banners on specified hosts.
This tool is intended for educational and authorized testing purposes only.

✨ Features

Scan a single IP or multiple targets at once.

Specify how many ports to scan (starting from port 1).

Automatically resolves hostnames to IP addresses.

Attempts to grab service banners for open ports.

⚠️ Legal Disclaimer

This tool is built for educational purposes and authorized security testing only.
Do not scan networks you don’t own or have explicit permission to test.
The author is not responsible for misuse or damage.

🛠️ Requirements

Python 3.x

IPy
 module

Install dependencies:

pip install IPy

🚀 Usage

Clone this repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Run the script:

python3 portscanner.py


Input your targets when prompted:

For a single target:

[+] Enter target/s to scan(split multiple targets with ,): 192.168.1.1
[+] Enter amount of ports to scan(starting from 1): 1000


For multiple targets:

[+] Enter target/s to scan(split multiple targets with ,): 192.168.1.1, scanme.nmap.org
[+] Enter amount of ports to scan(starting from 1): 500


The script will list open ports and (if available) their banners.

📄 Example Output
[ *** Scanning Target: 192.168.1.1 *** ]
[!] Open port: 22 : SSH-2.0-OpenSSH_8.4
[!] Open port: 80
[!] Open port: 443 : HTTP/1.1 200 OK
[!] All the scans are completed!

📝 Notes

The scan starts from port 1 up to the number you specify.

Timeout per port is set to 0.5s (can be adjusted in code).

Banner grabbing may fail silently if a service does not respond.
