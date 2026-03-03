# SSH
```bash

# Creating public and private key
ssh-keygen # Enter all
service ssh start
cp id_rsa.pub authorized_keys

ssh edibauer@localhost

cat id_rsa_pwn.pub >> ~/.ssh/authorized_keys


>

```

# SSH V2
```bash
sudo apt install openssh
sudo systemctl status ssh
sudo systemctl start ssh

ssh-keygen # creating a public and private key
# id_rsa - private
# id_rsa.pub - public

# create a copy of public key like authorized_keys
cp id_rsa.pub authorized_keys

# attack machine
# create a private and public key, copy public jey like authorized key and put it into .ssh vitims machine 


```