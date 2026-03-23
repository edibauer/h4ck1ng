# Recon
```bash
route -n
# ans
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    600    0        0 wlan0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
172.18.0.0      0.0.0.0         255.255.0.0     U     0      0        0 br-7fc99e6665ea
172.19.0.0      0.0.0.0         255.255.0.0     U     0      0        0 br-22d85d536b2b
192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlan0

ping -c 1 192.168.1.1
mkdir {nmap,content,scripts,tmp,exploits}

# ALISES
alias cat='/usr/bon/batcat' # into .zshrc
source ~/.zshrc

# FUNCTIONS (into .zshrc)
function mkt(){
    mkdir {nmap,scripts,exploits}
}

function extractPorts(){
    echo -e "\n[PROC] Extracting information...\n"
    ip_address=$(cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u)
    open_ports=$(cat allPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS="/" | xargs | tr ' ' ',')

    echo -e "\t[*]IP Address: ${ip_address}"
    echo -e "\t[*]Open Ports: ${open_ports}"
 
    echo ${open_ports} | tr -d '\n' | xclip -sel clip

    echo -e "\n[INFO] Ports has been copied to clipboard"
}

# NMAP
nmap -p- --open -vvv -n -Pn 192.168.1.1 -oG allPorts

cat allPorts | grep -oP '\d{1,5}' # filtering by regular expression (only digits with len by 5)
cat allPorts | grep -oP '\d{1,5}/open' # filtering by '/open' string
cat allPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS="/" | xargs | tr ' ' ','
# ans
22,53,80,443,52869

nmap -sCV -p22,53,80,443,52869 192.168.1.1 -oN target

nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn 192.168.1.1 -oG allPorts

# portScan.sh
#+begin portScan.sh
   1   │ #!/bin/bash
   2   │ 
   3   │ # ./portScan.sh <ip_address>
   4   │ if [[ -z $1 ]]; then
   5   │   echo "[INFO] Uso: ./portScan <ip_address>"
   6   │   exit 1
   7   │ fi
   8   │ 
   9   │ # proc
  10   │ ip_address=$1
  11   │ for port in $(seq 1 65535); do
  12   │   timeout 1 bash -c "echo '' > /dev/tcp/${ip_address}/${port}" 2>/dev/null && echo "[+] Port: $port - OPEN" &
  13   │ done
  14   │ wait
#+endPortScan.sh

# hostDiscovery.sh
#+begin hostDiscovery.sh
  1   │ #!/bin/bash
   2   │ 
   3   │ for i in $(seq 1 255); do
   4   │   timeout 1 bash -c "ping -c 1 192.168.1.${i} > /dev/null 2>&1" && echo "Host 192.168.1.${i} - ACTIVE" &
   5   │ done
   6   │ wait
#+end hostDiscovery.sh

# LUA scrips
locate .nse

# whichSystem.py
#+begin wichSystem.py
   3   │ import re
   4   │ import sys
   5   │ import subprocess
   6   │ 
   7   │ if len(sys.argv) != 2:
   8   │     print("\n [!] Uso: python3 " + sys.argv[0] + " <direccion_ip>\n")
   9   │     sys.exit(1)
  10   │ 
  11   │ def get_ttl(ip_address):
  12   │     proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=s
       │ ubprocess.PIPE, shell=True)
  13   │     (out,err) = proc.communicate()
  14   │ 
  15   │     out = out.split()
  16   │     out_ttl = out[12].decode('utf-8')
  17   │ 
  18   │     ttl_value = re.findall(r"\d{1,3}", out_ttl)[0]
  19   │     return ttl_value
  20   │ 
  21   │ def get_os(ttl):
  22   │     ttl = int(ttl)
  23   │     if ttl >= 0 and ttl <= 64:
  24   │         return "Linux"
  25   │     elif ttl >= 65 and ttl <= 128:
  26   │         return "Windows"
  27   │     else:
  28   │         return "Not Found"
  29   │ 
  30   │ if __name__ == '__main__':
  31   │     ip_address = sys.argv[1]
  32   │     ttl = get_ttl(ip_address)
  33   │     so = get_os(ttl)
  34   │     print("%s (ttl -> %s): %s" % (ip_address,ttl,so))
#+end whichSystem.py

# MOVE SCRIPT TO PATH
chmod +x whichSystem.py
echo $PATH
mv whichSystem.py /usr/bin

whichSystem.py # runs everywhere

# WFUZZ
wfuzz -c -t 300 --hc=404 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt http://192.168.1.1/FUZZ
# where
# -c: Colorized
# -t: threads
# --hc: hide code
# -L: Follow at redirect
# --sc: show code
# --hl:hide lines
# --hh: hide characters

wfuzz -c -t 300 --hc=404 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -w extensions.txt http://192.168.1.1/FUZZ.FUZ2Z # Use tu search file extensions

# etc hosts
nano /etc/hosts
10.10.10.46 apocalypse.htb

# Web Aplication Firewall
wafwoof http://10.10.10.46

# WPSCAN
wpscan --url http://10.10.10.46 -e vp,u


```