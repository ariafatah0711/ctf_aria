---
layout: default
level: 14
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. \
For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level.

Note: localhost is a hostname that refers to the machine you are working on

# ssh
```bash
sshpass -p "FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn" ssh -o StrictHostKeyChecking=no bandit13@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
ls -la sshkey.private 
# -rw-r----- 1 bandit14 bandit13 1679 Sep 19 07:08 sshkey.private

ssh -i sshkey.private bandit14@localhost -p 2220 # login ssh with private key

cat /etc/bandit_pass/bandit14
# MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

# flag
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS