---
layout: level
level: 26
previous: ./level 25.html
next: ./level 27.html
---

# soal
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

# solve
```bash
cat bandit26.sshkey
# -----BEGIN RSA PRIVATE KEY-----
# ...

## ssh in host
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 -vvv

## i try another option but not work
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 -t /bin/sh # change the tty
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220 -T # tanpa tty
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p 2220  "whoami" # run command
ssh -i bandit26.sshkey bandit26@bandit.labs.overthewire.org -p ^C20 -t /bin/sh "cat /etc/bandit_pass/bandit26 > /tmp/tmp.nvaRc1Ef3g/pass" # input only
```

- namun kareana saya sudah mencoba namun tidak ada yang berhasil jadi saya mencari di youtube dan mencari solusinya
- disini saya menemukan solusi dengan mengecilkan layar maka nanti kita seolah seolah sedang menggunakan perintah less
  ```ssh -i bandit26 bandit26@localhost -p 2220```
  ![alt text](docs/images/image-1.png)
  ![alt text](docs/images/image.png)
- jika sudah kita bisa click "v" untuk masuk ke vim editor
- jika sudah kita bisa cari tau cara keluar dari vim dan masuk ke shell di gtfobins
  ![alt text](docs/images/image-2.png)
  - https://gtfobins.github.io/gtfobins/vim/
  - kita coba salah satunya dengan mengclick ESC terlebih dahulu
    ```bash
    :set shell=/bin/sh|:shell
    ```
- atau kita bisa gunakan langkah satu persatu saat sudah di vim
  ```bash
  :set shell=/bin/bash 
  # lalu enter

  :shell
  # ini ssama seperti sebelumnya hanya saja kita secara 1 persatu
  # jika ingin cepat kita bisa gunakan |

  :set shell=/bin/bash | :shell
  ```

- got flag
  ```bash
  cat /etc/bandit_pass/bandit26
  # s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
  ```

# flag
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ