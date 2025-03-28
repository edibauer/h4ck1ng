#!/bin/bash

function ctrl_c() {
    echo -e "\n\n [!] Saliendo..."
    tput cnorm; exit 1
}

# ctrl + c 
trap ctrl_c SIGINT

old_process=$(ps -eo user,command)

tput civis # hide cursor

while true; do
    new_process=$(ps -eo user,command)
    diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -vE "command|kworker|procmon"

done