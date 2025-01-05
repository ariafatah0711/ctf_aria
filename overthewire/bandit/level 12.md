---
layout: default
level: 12
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

# solve
```bash
cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
# The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

# flag
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4