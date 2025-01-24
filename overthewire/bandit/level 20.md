---
layout: default
level: 20
name_file: level
---

{% include level-section.html %}

# soal
To gain access to the next level, you should use the setuid binary in the homedirectory. \
Execute it without arguments to find out how to use it. \
The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

# ssh
```bash
sshpass -p "cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8" ssh -o StrictHostKeyChecking=no bandit19@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
ls -la bandit20-do 
# -rwsr-x--- 1 bandit20 bandit19 14880 Sep 19 07:08 bandit20-do
# suid -r => file ini bisa dijalankan siapapun namun dengan id si pemilik file tersebut
## misal jika terdapat user membuat file run linux dengan suid maka ketika user lain me run file itu.tersebut
## maka seolah olah mereka menggunakan user owner

./bandit20-do
# Run a command as another user.
#  Example: ./bandit20-do id

/bandit20-do whoami
# bandit20
# disini bisa kita lihat padahal kita adalah user bandit19 namun ketika di whoami output yang muncul adalah bandit20

cat /etc/bandit_pass/bandit20 # whitout file suid
# cat: /etc/bandit_pass/bandit20: Permission denied

./bandit20-do cat /etc/bandit_pass/bandit20 # with file suid
# 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

# flag
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO