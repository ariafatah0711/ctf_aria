---
layout: default
level: 1
name_file: level
---

{% include level-section.html %}

# soal
Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

S1JZUFRPTklTR1JFQVQ= \
Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/

# solve
```bash
echo S1JZUFRPTklTR1JFQVQ= | base64 -d
# KRYPTONISGREAT
```

# flag
KRYPTONISGREAT