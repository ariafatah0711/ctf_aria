---
layout: default
level: 8
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt next to the word millionth

# ssh
```bash
sshpass -p "morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj" ssh -o StrictHostKeyChecking=no bandit7@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
cat data.txt | grep -i millionth
# millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

# flag
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc