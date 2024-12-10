---
layout: level
level: 5
previous: ./level 04.html
next: ./level 06.html
---

# soal
The password for the next level is stored in the only human-readable file in the inhere directory. \
Tip: if your terminal is messed up, try the “reset” command.

# solve
```bash
cd inhere/
grep -r ../
# grep: -file06: binary file matches
# bandit4@bandit:~/inhere$ grep -r ../.
# bandit4@bandit:~/inhere$ grep -r .
# grep: -file08: binary file matches
# grep: -file02: binary file matches
# grep: -file09: binary file matches
# grep: -file01: binary file matches
# grep: -file00: binary file matches
# grep: -file05: binary file matches
# -file07:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
# -file03:d
# grep: -file03: binary file matches
# grep: -file06: binary file matches
# grep: -file04: binary file matchis
```

# flag
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw