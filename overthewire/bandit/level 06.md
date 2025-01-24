---
layout: default
level: 6
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable \
1033 bytes in size \
not executable

# ssh
```bash
sshpass -p "4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw" ssh -o StrictHostKeyChecking=no bandit5@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
find . -size 1033c -readable ! -perm 111
find . -size 1033c -readable ! -executable
cat ./inhere/maybehere07/.file2
```

# flag
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG