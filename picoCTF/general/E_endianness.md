# soal
Know of little and big endian? \
Source \
Additional details will be available after launching your challenge instance.

## launch istance
Know of little and big endian? \
Source \
nc titan.picoctf.net 54628

# hint
- You might want to check the ASCII table to first find the hexadecimal representation of characters before finding the endianness.
- Read more about how endianness here

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/119/flag.c

nc titan.picoctf.net 54628
# Welcome to the Endian CTF!
# You need to find both the little endian and big endian representations of a word.
# If you get both correct, you will receive the flag.
# Word: kssra
Enter the Little Endian representation: 617273736B
# Correct Little Endian representation!
Enter the Big Endian representation: 6b73737261
# Correct Big Endian representation!
# Congratulations! You found both endian representations correctly!
# Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_28329f0a}

for i in "kssra":
    print(hex(ord(i)))
# 0x6b
# 0x73
# 0x73
# 0x72
# 0x61

for i in "kssra":
    print(hex(ord(i)).lstrip("0x"))
# 6b
# 73
# 73
# 72
# 61

for i in "kssra":
    print(hex(ord(i)).lstrip("0x"), end="")
# 6b73737261

## convert hex decimal menjadi little endian
## https://www.save-editor.com/tools/wse_hex.html
## atau sebenernya kita bisa balik teksnya

# BIG ENDIAN => LITTLE ENNDIAN
# 6b73737261 => 617273736B
# 6b 73 73 72 61 => 61 72 73 73 6b
```

# flag
picoCTF{3ndi4n_sw4p_su33ess_28329f0a}