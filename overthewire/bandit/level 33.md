---
layout: default
level: 33
name_file: level
---

{% include level-section.html %}

# soal
After all this git stuff, it’s time for another escape. Good luck!

# ssh
```bash
sshpass -p "3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K" ssh -o StrictHostKeyChecking=no bandit32@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
WELCOME TO THE UPPERCASE SHELL
>> ls
sh: 1: LS: not found
>> LS
sh: 1: LS: not found

# all command use uppercase
# i can use $0 is represen bash

$ cat /etc/bandit_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```

## $0
```bash
➜ ~  echo $0
bash

➜ ~  echo $1
```

# flag
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0