---
layout: default
level: 27
name_file: level
---

{% include level-section.html %}

# soal
Good job getting a shell! Now hurry and grab the password for bandit27!

# ssh
```bash
sshpass -p "s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ" ssh -o StrictHostKeyChecking=no bandit26@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
 ls -la bandit27-do
# -rwsr-x--- 1 bandit27 bandit26 14880 Sep 19 07:08 bandit27-do
./bandit27-do
# Run a command as another user.
#  Example: ./bandit27-do id

## ini sama seperti tantangan sebelumnya karena ini adalah SUID bandit27

./bandit27-do whoami
# bandit27
./bandit27-do cat /etc/bandit_pass/bandit27
# upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```

## solve auto but not work
```bash
#!/bin/bash

echo "[+] Starting automated SSH connection with Vim handling"

# Set password and server information
PASSWORD="iCi86ttT4KSNe1armKiwbQNmB3YJP3q4"
SERVER="bandit.labs.overthewire.org"
PORT=2220
USER="bandit25"

# Jalankan SSH dengan alokasi terminal interaktif dan bypass host key verification
sshpass -p "$PASSWORD" ssh -tt -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null "$USER@$SERVER" -p "$PORT" <<EOF
ssh -tt -i bandit26.sshkey -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null bandit26@localhost -p 2220
EOF

echo "[+] SSH session completed"
```

# flag
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB