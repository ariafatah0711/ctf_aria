---
layout: default
level: 16
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL/TLS encryption.

Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.

# ssh
```bash
sshpass -p "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" ssh -o StrictHostKeyChecking=no bandit15@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
## ncat
echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | ncat --ssl localhost 30001
# Correct!
# kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```

## another option but didn't work 
```bash
echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | openssl s_client -connect localhost:30001
# CONNECTED(00000003)
# Can't use SSL_get_servername
```

# flag
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx