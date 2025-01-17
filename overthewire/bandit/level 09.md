---
layout: default
level: 9
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

# ssh
```bash
sshpass -p "dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc" ssh -o StrictHostKeyChecking=no bandit8@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
sort data.txt | uniq -u
```

# flag
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM