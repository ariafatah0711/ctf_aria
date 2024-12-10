---
layout: level
level: 6
previous: ./level 05.html
next: ./level 07.html
---

# soal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable \
1033 bytes in size \
not executable

# solve
```bash
find . -size 1033c ! -perm 111
cat ./maybehere07/.file2
```

# flag
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG