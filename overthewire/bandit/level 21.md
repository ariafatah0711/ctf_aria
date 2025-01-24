---
layout: default
level: 21
name_file: level
---

{% include level-section.html %}

# soal
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. \
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). \
If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

# ssh
```bash
sshpass -p "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" ssh -o StrictHostKeyChecking=no bandit20@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
ls -la suconnect 
# -rwsr-x--- 1 bandit21 bandit20 15604 Sep 19 07:08 suconnect

nc -lvnp 30005
# Listening on 0.0.0.0 30005
# Connection received on 127.0.0.1 51362
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
# EeoULMCra2q0dSkYj561DX7s1CpBuOBt

./suconnect 30005
# Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
# Password matches, sending next password

## cara kerjanya adalah dengan membuat sebuah listener pada port tertentu untuk mendengarkan port
## lalu kita hanya perlu menconnect dengan file suid suconnect dengan port yang sama
## lalu kita hanya perlu memasukan password yang saat ini dari listen untuk mendapatkan password yang akan di kirim suconnect
```

# flag
EeoULMCra2q0dSkYj561DX7s1CpBuOBt