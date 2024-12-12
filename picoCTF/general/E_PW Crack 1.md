# soal
Can you crack the password to get the flag? \
Download the password checker here and you'll need the encrypted flag in the same directory too.

# hint
- To view the file in the webshell, do: $ nano level1.py
- To exit nano, press Ctrl and x and follow the on-screen prompts.
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/11/level1.py
wget https://artifacts.picoctf.net/c/11/level1.flag.txt.enc

cat level1.py
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "1e1a"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
###

python3 level1.py
# Please enter correct password for flag: 1e1a
# Welcome back... your flag, user:
# picoCTF{545h_r1ng1ng_fa343060}
```

# flag
picoCTF{545h_r1ng1ng_fa343060}