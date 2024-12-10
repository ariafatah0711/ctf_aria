---
layout: level
level: 8
previous: ./level 07.html
next: ./level 09.html
---

# soal
The password for the next level is stored in the file data.txt next to the word millionth

# solve
```bash
cat data.txt | grep -i millionth
# millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

# flag
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc