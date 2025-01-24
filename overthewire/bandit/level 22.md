---
layout: default
level: 22
name_file: level
---

{% include level-section.html %}

# soal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

# ssh
```bash
sshpass -p "EeoULMCra2q0dSkYj561DX7s1CpBuOBt" ssh -o StrictHostKeyChecking=no bandit21@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
ls -la /etc/cron.d/
# -rw-r--r--   1 root root   120 Sep 19 07:08 cronjob_bandit22
# -rw-r--r--   1 root root   122 Sep 19 07:08 cronjob_bandit23
# -rw-r--r--   1 root root   120 Sep 19 07:08 cronjob_bandit24

cat /etc/cron.d/cronjob_bandit22
# @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
# * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

cat /usr/bin/cronjob_bandit22.sh
###
#!/bin/bash

chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
###

cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
# tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

# flag
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q