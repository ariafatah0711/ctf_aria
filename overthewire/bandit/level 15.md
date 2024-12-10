---
layout: level
level: 15
previous: ./level 14.html
next: ./level 16.html
---

# soal
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

# solve
```bash
## netcat / nc
echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | nc localhost 30000
# Correct!
# 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

## telnet
telnet localhost 30000
# Trying 127.0.0.1...
# Connected to localhost.
# Escape character is '^]'.
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
# Correct!
# 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

# Connection closed by foreign host

## sockat
echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS" | socat - TCP:localhost:30000
# Correct!
# 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

- or you can use python but here after i tried it it didn't work
```py
import socket

HOST = 'localhost'
PORT = 3000
data = "data"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())
    response = s.recv(1024)
    print("Received:", response.decode())
```

## another option but didn't work 
```bash
# curl for POST web
curl -X POST -d "data" http://localhost:3000

# curl if not web
curl telnet://localhost:3000 --data "data"

# bash /dev/tcp
echo "data" > /dev/tcp/localhost/3000

# openssl
echo "data" | openssl s_client -connect localhost:3000 # only secure layer (ssl/tls)
```

# flag
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo