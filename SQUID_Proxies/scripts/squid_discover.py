import sys, signal, requests

def def_handler(sig, frame):
    print("\n\n[!] Quitting...")
    sys.exit(1)

# ctrl + c
signal.signal(signal.SIGINT, def_handler)

main_url = "http://127.0.0.1"
squid_proxy = {'http': 'http://192.168.1.10:3128'}

def port_discovery():
    tcp_ports = {
    1, 7, 9, 13, 17, 19, 20, 21, 22, 23, 
    25, 37, 43, 53, 79, 80, 88, 109, 110, 111, 
    113, 119, 135, 139, 143, 161, 179, 389, 443, 445, 
    465, 500, 514, 515, 548, 554, 587, 636, 989, 990, 
    993, 995, 1080, 1194, 1433, 1521, 1723, 2049, 3306, 3389, 
    5432, 5900, 8080
    }

    for tcp_port in tcp_ports:
        r = requests.get(f"{main_url}:{str(tcp_port)}", proxies=squid_proxy)

        if r.status_code == 200:
            print("[+] Port %s -> open" % tcp_port)

if __name__ == '__main__':
    port_discovery()
