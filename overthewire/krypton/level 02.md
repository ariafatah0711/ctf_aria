---
layout: default
level: 2
name_file: level
---

{% include level-section.html %}

# soal
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. \
It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. \
This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

# ssh
```bash
sshpass -p "KRYPTONISGREAT" ssh -o StrictHostKeyChecking=no krypton1@krypton.labs.overthewire.org -p 2231

# scp
sshpass -p "KRYPTONISGREAT" scp -R -P 2231 krypton1@krypton.labs.overthewire.org:/krypton/krypton1/* krypton1
```

# solve
```bash
cd /krypton/krypton1
cat krypton2 
# YRIRY GJB CNFFJBEQ EBGGRA

echo "YRIRY GJB CNFFJBEQ EBGGRA" | tr '[N-ZA-M]' '[A-Z]'                   
# LEVEL TWO PASSWORD ROTTEN
```

## ROT 13
- caesar chiper shift 13 / ROT 13

# flag
ROTTEN