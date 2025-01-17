---
layout: default
level: 4
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in a hidden file in the inhere directory.

# ssh
```bash
sshpass -p "MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx" ssh -o StrictHostKeyChecking=no bandit3@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
cat inhere/...Hiding-From-You
```

# flag
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ