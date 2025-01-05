---
layout: level
level: 27
previous: ./level 26.html
next: ./level 28.html
---

# soal
Good job getting a shell! Now hurry and grab the password for bandit27!

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

# flag
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB