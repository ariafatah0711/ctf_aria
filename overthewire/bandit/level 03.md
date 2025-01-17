---
layout: default
level: 3
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in a file called spaces in this filename located in the home directory

# ssh
```bash
sshpass -p "263JGJPfgU6LtdEvgfWU1XP5yac29mFx" ssh -o StrictHostKeyChecking=no bandit2@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
cat 'spaces in this filename'
cat ./spaces\ in\ this\ filename
cat spaces\ in\ this\ filename
```

# flag
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx