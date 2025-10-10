### squid
```bash
# download SickOS Machine
nmap -p- --open --min-rate 5000 -sS -vvv -n -Pn 192.168.1.10 -oG allPorts

nmap -p- --open --min-rate 5000 -sS -n -Pn -vvv 192.168.1.10 -oG allPorts

nmap -sCV -p22,3128 192.168.1.10 -oN targeted

# nmap filtered ports
curl http://192.168.1.10 --proxy http://192.168.1.10:3128

# ans
<h1>
BLEHHH!!!
</h1>

# config in foxy proxy 192.168.1.10 -p 3128
gobuster dir -u http://192.168.1.10 --proxy http://192.168.1.10:3128 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 20




```