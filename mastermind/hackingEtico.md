### Creacion y gestion de usuarios
```bash
cat /etc/passwd | grep "sh$" # $ - end with
cat /etc/passwd | grep "sh$" | awk -F':' '{print $1}'

whoami
# ans
edibuaer

id
# ans
uid=1000(edibauer) gid=1000(edibauer) groups=1000(edibauer),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),116(bluetooth),119(lpadmin),124(wireshark),131(kaboxer)

# ADDING USER
sudo su
mkdir pepito
useradd -d /home/pepito -s /bin/bash pepito

# SETTING PASSWORD
passwd pepito

# SETTING OWNER
chown pepito pepito
# ans
total 24
drwx------ 31 edibauer edibauer  4096 Mar  7 22:45 edibauer
drwx------  2 root     root     16384 Jan 10 18:53 lost+found
drwxr-xr-x  2 pepito   root      4096 Mar  7 22:46 pepito

# SETTING GROUP
chgrp pepito pepito
# ans
total 24
drwx------ 31 edibauer edibauer  4096 Mar  7 22:45 edibauer
drwx------  2 root     root     16384 Jan 10 18:53 lost+found
drwxr-xr-x  2 pepito   pepito    4096 Mar  7 22:46 pepito

chown root:edibauer pepito
chown pepito:pepito pepito

su pepito
id
#ans
uid=1001(pepito) gid=1001(pepito) groups=1001(pepito) # not in sudoers file

```
### Asignacion e intepretacion de permisos
```bash
su pepito

mkdir directorio
ls -l
# ans
total 4
drwxrwxr-x 2 pepito pepito 4096 Mar  7 23:04 directorio

exit
whoami
# ans
edibauer

cd /home/pepito/directorio
touch file.txt
# ans
touch: cannot touch 'archivo.txt': Permission denied

# ADDING PERMISSIONS
sudo su
chmod o+w directorio
ls -l
# ans
total 4
drwxrwxrwx 2 pepito pepito 4096 Mar  7 23:04 directorio

chmod o-w directorio
ls -l
# ans
total 4
drwxrwxr-x 2 pepito pepito 4096 Mar  7 23:04 directorio

chmod g+w directorio
chmod g-w,o+w directorio

# ADDING GROUP PERMISSIONS
su pepito
mkdir directorio
# ans
total 4
drwxrwxr-x 2 pepito pepito 4096 Mar  8 00:27 directorio

sudo su
groupadd colegio
cat /etc/group | tail -n 1
#ans
colegio:x:1002:

chgrp colegio directorio
ls -l
# ans
total 4
drwxrwxr-x 2 pepito colegio 4096 Mar  8 00:27 directorio

# ADDING USER INTO A GROUP
usermod -a -G colegio edibauer
id edibauer
# ans
uid=1000(edibauer) gid=1000(edibauer) groups=1000(edibauer),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),116(bluetooth),119(lpadmin),124(wireshark),131(kaboxer),1002(colegio)

chmod g-rwx directorio

su edibauer
cd directorio
# ans
cd: permission denied: directorio

```
