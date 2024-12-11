# soal
Reverse this linux executable? \
binary

# hint
- What can we do to reduce the size of a binary after compiling it.

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/22/out
chmod +x out

./out
# Enter the password to unlock this file: 123
# You entered: 123

# Access denied

file out
# out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header

strings out
# ...
# UPX!
# UPX!

upx-ucl -d out
upx -d out
#                       Ultimate Packer for eXecutables
#                           Copyright (C) 1996 - 2020
# UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

#         File size         Ratio      Format      Name
#    --------------------   ------   -----------   -----------
#    872088 <-    336512   38.59%   linux/amd64   out

# Unpacked 1 file.

strings out | grep flag
# Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f35646565343434317d
```

- deocde the code
  ```bash
  "7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f35646565343434317d".decode("hex")
  # 'picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_5dee4441}'

  codecs.decode("7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f35646565343434317d", "hex")
  # b'picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_5dee4441}'
  ```

# flag
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_5dee4441}