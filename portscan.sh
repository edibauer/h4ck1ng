#!/bin/bash

 function ctrl_c() {
    echo -e "\n\n[!] Saliendo... \n"
    tput cnorm; exit 1
 }

 # ctrl_c
 trap ctrl_c SIGINT

 # sleep 12

 declare -a ports=( $(seq 1 65535) )

function checkPort() {
    (exec 3<> /dev/tcp/$1/$2) 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "[+] Host $1 - Port $2 (OPEN)"
    fi

    exec 3<&-
    exec 3<&-

}

tput civis # hide cursor

 if [ $1 ]; then
    for port in ${ports[@]}; do
    # echo $port
    checkPort $1 $port & # &-segundo plano
    done
 else
    echo -e "\n[+] Uso: $0 ipaddress \n"
 fi

 wait

 tput cnorm

