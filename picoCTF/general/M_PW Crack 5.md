# soal
Can you crack the password to get the flag? \
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. \
Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

# hint
- Opening a file in Python is crucial to using the provided dictionary.
- You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, strip
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/32/level5.py
wget https://artifacts.picoctf.net/c/32/level5.flag.txt.enc
wget https://artifacts.picoctf.net/c/32/level5.hash.bin
wget https://artifacts.picoctf.net/c/32/dictionary.txt

cat level5.flag.txt.enc
# G
# V      t1s_QhYWP:VQWTH

cat level5.hash.bin
# �5.v�`��f/pߚ

head dictionary.txt
# 0000
# 0001

python3 level5.py
# Please enter correct password for flag: 0000
# That password is incorrect

## sama seperrti sebelumnya hanya saja password yang dibutuhkan adalah teks yang ada pada file
```

- saya tambahkan code untuk open file dan mencoba untuk melakukan looping
  ```py
  pw_list = open('dictionary.txt').read().split()
  for i in pw_list:
    # print(i)
    decryption = str_xor(flag_enc.decode(), i)
    print(decryption)
  ```

- dan ini hasilnya ketika di run
  ```bash
  python3 level5.py | grep pico
  # grep: (standard input): binary file matches

  python3 level5.py | grep --text pico
  # qjf=BWC)i70:^picod4<f\1bg13492x
  # picoCTF{h45h_sl1ng1ng_40f26f81}
  ```

# flag
picoCTF{h45h_sl1ng1ng_40f26f81}