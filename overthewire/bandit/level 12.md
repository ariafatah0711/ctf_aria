---
layout: level
level: 12
previous: ./level 11.html
next: ./level 13.html
---

# soal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

# solve
```bash
cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
# The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

# flag
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4