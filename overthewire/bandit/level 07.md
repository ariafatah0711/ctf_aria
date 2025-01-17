---
layout: default
level: 7
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7 \
owned by group bandit6 \
33 bytes in size

# ssh
```bash
sshpass -p "HWasnPhtq9AVKe0dmk45nxy20cvUa6EG" ssh -o StrictHostKeyChecking=no bandit6@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
# /var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
```

# flag
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj