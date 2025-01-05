---
layout: default
level: 23
name_file: level
---

{% include level-section.html %}

# soal
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. \
If you are having problems understanding what it does, try executing it to see the debug information it prints.

# solve
- check cronjob file
    ```bash
    cd /etc/cron.d
    cat cronjob_bandit23
    # @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
    # * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
    ```

- cat /usr/bin/cronjob_bandit23.sh
    ```bash
    #!/bin/bash

    myname=$(whoami)
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
    echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
    cat /etc/bandit_pass/$myname > /tmp/$mytarget
    ```

- try running the file for debuging
    ```bash
    /usr/bin/cronjob_bandit23.sh
    # Copying passwordfile /etc/bandit_pass/bandit22 to /tmp/8169b67bd894ddbb4412f91573b38db3

    cat /tmp/8169b67bd894ddbb4412f91573b38db3
    # tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

    ## but after i try the flag is not the password for bandit23
    ```

- modification the file
    ```bash
    ## try running with the modification file
    workdir=$(mktemp -d); cd $workdir
    cp /usr/bin/cronjob_bandit23.sh .

    cat ./cronjob_bandit23.sh
    ######
    #!/bin/bash

    myname="bandit23" # change the value
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

    echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

    # cat /etc/bandit_pass/$myname > /tmp/$mytarget
    ######

    ./cronjob_bandit23.sh
    # Copying passwordfile /etc/bandit_pass/bandit23 to /tmp/8ca319486bfbbc3663ea0fbe81326349

    cat /tmp/8ca319486bfbbc3663ea0fbe81326349
    # 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
    ```

# flag
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga