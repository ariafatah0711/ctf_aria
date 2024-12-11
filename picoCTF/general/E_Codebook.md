# soal
Run the Python script code.py in the same directory as codebook.txt. \
Download code.py \
Download codebook.txt

# hint
- On the webshell, use ls to see if both files are in the directory you are in
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/1/code.py
wget https://artifacts.picoctf.net/c/1/codebook.txt

cat codebook.txt
# azbycxdwevfugthsirjqkplomn

python3 code.py
# picoCTF{c0d3b00k_455157_d9aa2df2}
```

# flag
picoCTF{c0d3b00k_455157_d9aa2df2}