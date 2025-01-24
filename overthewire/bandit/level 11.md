---
layout: default
level: 11
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt, which contains base64 encoded data

# ssh
```bash
sshpass -p "FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey" ssh -o StrictHostKeyChecking=no bandit10@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
cat data.txt | base64 -d
# The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

# flag
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr