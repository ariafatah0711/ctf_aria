# soal
Can you crack the password to get the flag? \
Download the password checker here and you'll need the encrypted flag in the same directory too.

# hint
- Does that encoding look familiar?
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/13/level2.py
wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc

cat level2.py
# user_pw = input("Please enter correct password for flag: ")
#    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):

python3 -c "print(chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))"
# de76

python3 level2.py
# Please enter correct password for flag: de76
# Welcome back... your flag, user:
# picoCTF{tr45h_51ng1ng_489dea9a}
```

# flag
picoCTF{tr45h_51ng1ng_489dea9a}