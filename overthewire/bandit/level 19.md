---
layout: default
level: 19
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

# ssh
```bash
sshpass -p "x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO" ssh -o StrictHostKeyChecking=no bandit18@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
# Byebye !
# Connection to bandit.labs.overthewire.org closed.

## You need to change the shell with /bin/sh
## because in .bashrc it has been modified to exit when we log in
ssh bandit18@bandit.labs.overthewire.org -p 2220 -t /bin/sh 
cat readme  
# cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

## or u can ssh with command cat
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
# cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

## ir y can with scp for download file readme
scp -P 2220 bandit18@bandit.labs.overthewire.org:~/readme .
cat readme # cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

## or use sftp
sftp -P 2220 bandit18@bandit.labs.overthewire.org
sftp> get readme
# Fetching /home/bandit18/readme to readme
# readme  100%   33     0.1KB/s   00:00 
cat readme # cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

## or auto
sshpass -p "x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO" ssh -o StrictHostKeyChecking=no bandit18@bandit.labs.overthewire.org -p 2220 -t /bin/sh
sshpass -p "x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO" ssh -o StrictHostKeyChecking=no bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

# flag
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8