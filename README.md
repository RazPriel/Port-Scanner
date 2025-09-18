# 🔎 Simple Python Port Scanner

A lightweight Python-based port scanner that checks for open ports and grabs service banners on specified hosts.  

## ✨ Features

- Scan a single IP or multiple targets at once.
- Specify how many ports to scan (starting from port 1).
- Automatically resolves hostnames to IP addresses.
- Attempts to grab service banners for open ports.

## 🛠️ Requirements

- Python 3.x
- [IPy](https://pypi.org/project/IPy/) module  

Install dependencies:

```bash
pip install IPy
```

## 🚀 Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Run the script:

```bash
python3 portscanner.py
```

3. Input your targets when prompted:  

- For a single target:

```
[+] Enter target/s to scan(split multiple targets with ,): 192.168.1.1
[+] Enter amount of ports to scan(starting from 1): 1000
```

- For multiple targets:

```
[+] Enter target/s to scan(split multiple targets with ,): 192.168.1.1, scanme.nmap.org
[+] Enter amount of ports to scan(starting from 1): 500
```

4. The script will list open ports and (if available) their banners.

## 📄 Example Output

```
[ *** Scanning Target: 192.168.1.1 *** ]
[!] Open port: 22 : SSH-2.0-OpenSSH_8.4
[!] Open port: 80
[!] Open port: 443 : HTTP/1.1 200 OK
[!] All the scans are completed!
```

## 📝 Notes

- The scan starts from port **1** up to the number you specify.
- Timeout per port is set to **0.5s** (can be adjusted in code).
- Banner grabbing may fail silently if a service does not respond.
