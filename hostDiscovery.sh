#!/bin/bash

function ctrl_C() {
    echo -e "\n\n[!] Saliendo..."
    tput cnorm; exit 1
}

tput civis

# ctrl c
trap ctrl_c SIGINT

for i in $(seq 1 254) ; do
    timeout 1 bash -c "ping -c 1 192.168.100.$1" &>/dev/null && echo "[+] Host 192.168.100.$i - ACTIVE" & # & ? threads
done

wait
tput cnorm 