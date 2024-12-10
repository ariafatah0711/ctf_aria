---
layout: level
level: 7
previous: ./level 06.html
next: ./level 08.html
---

# soal
The password for the next level is stored somewhere on the server and has all of the following properties: \

owned by user bandit7 \
owned by group bandit6 \
33 bytes in size \

# solve
```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
# /var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
```

# flag
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj