# soal
Can you crack the password to get the flag? \
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. \
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# hint
- To view the level3.hash.bin file in the webshell, do: $ bvi level3.hash.bin
- To exit bvi type :q and press enter.
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/18/level3.py
wget https://artifacts.picoctf.net/c/18/level3.flag.txt.enc
wget https://artifacts.picoctf.net/c/18/level3.hash.bin

cat level3.flag.txt.enc
# B[ZZqfN_
# ...

cat level3.hash.bin
# m`��TA
#      45���&

python3 level3.py
# Please enter correct password for flag: 8799
# That password is incorrect
```

- ketika saya cek di file python nya ternyata terdapat sebuah function pengecekan, dan dibawahnya terrdapat sebuah list password yang sudah pasti benar
  - dan saya mencoba untuk melakukan looping dengan function tersebut
    ```py
    def level_3_pw_check(user_pw): # tambahkan paramter user_pw
        # user_pw = input("Please enter correct password for flag: ")
        user_pw_hash = hash_pw(user_pw)
    
    pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

    for i in pos_pw_list:
        level_3_pw_check(i)
    ```

- dan ketika saya run 
  ```bash
  python3 level3.py
  # That password is incorrect
  # That password is incorrect
  # That password is incorrect
  # That password is incorrect
  # Welcome back... your flag, user:
  # picoCTF{m45h_fl1ng1ng_6f98a49f}
  # That password is incorrect
  # That password is incorrect
  ```

# flag
picoCTF{m45h_fl1ng1ng_6f98a49f}