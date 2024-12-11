# soal
Can you look at the data in this binary: static? This BASH script might help!

# solve
```bash
wget https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static
wget https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh

file static
# static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=639391a8b15c579d69659462d3c935fa61693f17, not stripped

strings static | grep pico
# picoCTF{d15a5m_t34s3r_98d35619}

cat ltdis.sh
###
#!/bin/bash

objdump -Dj .text $1 > $1.ltdis.x86_64.txt
if [ -s "$1.ltdis.x86_64.txt" ]
then
        echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"
        echo "Ripping strings from binary with file offsets..."
        strings -a -t x $1 > $1.ltdis.strings.txt
        echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"
else
        echo "Disassembly failed!"
        echo "Usage: ltdis.sh <program-file>"
        echo "Bye!"
fi
###

chmod +x ltdis.sh
./ltdis.sh static

strings static.ltdis.strings.txt | grep pico
# 1020 picoCTF{d15a5m_t34s3r_98d35619}
```

# flag
picoCTF{d15a5m_t34s3r_98d35619}