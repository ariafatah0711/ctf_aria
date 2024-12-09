# soal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

# solve
```bash
ls -la /etc/cron.d/
# -rw-r--r--   1 root root   120 Sep 19 07:08 cronjob_bandit22
# -rw-r--r--   1 root root   122 Sep 19 07:08 cronjob_bandit23
# -rw-r--r--   1 root root   120 Sep 19 07:08 cronjob_bandit24

cat /etc/cron.d/cronjob_bandit22
# @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
# * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null


```

# flag
