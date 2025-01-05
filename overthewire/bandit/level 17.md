---
layout: level
level: 17
previous: ./level 16.html
next: ./level 18.html
---

# soal
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. \
First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. \
There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

# solve
- check the port open with nmap
    ```bash
    nmap -p 31000-32000 localhost
    # Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-12-09 13:14 UTC
    # Nmap scan report for localhost (127.0.0.1)
    # Host is up (0.00013s latency).
    # Not shown: 995 closed tcp ports (conn-refused)
    # PORT      STATE    SERVICE
    # 31046/tcp open     unknown
    # 31518/tcp open     unknown
    # 31691/tcp open     unknown
    # 31700/tcp filtered unknown
    # 31790/tcp open     unknown
    # 31960/tcp open     unknown

    # Nmap done: 1 IP address (1 host up) scanned in 1.26 seconds

    echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | ncat --ssl localhost 31046
    # Ncat: Input/output error.

    echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | ncat --ssl localhost 31518
    # kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
    ## this cred for bandit16

    echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | ncat --ssl localhost 31691
    # Ncat: Input/output error.

    echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | ncat --ssl localhost 31790
    # Correct!
    # -----BEGIN RSA PRIVATE KEY-----
    # MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
    # ...
    # -----END RSA PRIVATE KEY-----
    ```

- login with id_rsa
    ```bash
    workdir=$(mktemp -d)
    cd $workdir
    vi id_rsa

    ssh -i id_rsa bandit17@localhost -p 2220
    # Permissions 0664 for 'id_rsa' are too open.

    # if u got error WARNING: UNPROTECTED PRIVATE KEY FILE!
    # change the private key permissions 600 (user:read, group:no, other:no)
    chmod 600 id_rsa
    ## ur need delete permission for group and other
    ## and minimal permission read

    ssh -i id_rsa bandit17@localhost -p 2220

    cat /etc/bandit_pass/bandit17
    # EReVavePLFHtFlFsjn3hyzMlvSuSAcRD
    ```

# flag
EReVavePLFHtFlFsjn3hyzMlvSuSAcRD