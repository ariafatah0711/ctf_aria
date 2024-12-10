---
layout: level
level: 11
previous: ./level 10.html
next: ./level 12.html
---

# soal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

# solve
```bash
cat data.txt | base64 -d
# The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

# flag
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr