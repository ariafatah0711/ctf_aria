# soal
Unzip this archive and find the flag. \
Download zip file

# hint
- Can grep be instructed to look at every file in a directory and its subdirectories?

# solve
```bash
wget https://artifacts.picoctf.net/c/504/big-zip-files.zip

unzip big-zip-files.zip
cd big-zip-files/

grep -ri "pico"
# folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

# flag
picoCTF{gr3p_15_m4g1c_ef8790dc}