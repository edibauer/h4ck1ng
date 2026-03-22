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

```