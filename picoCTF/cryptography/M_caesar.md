# soal
Decrypt this message.

# hint
- caesar cipher tutorial

# solve
```
wget https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext
cat ciphertext
# picoCTF{dspttjohuifsvcjdpoabrkttds}

wget https://raw.githubusercontent.com/ariafatah0711/ctf_aria/refs/heads/main/tool/caesar
chmod +x caesar
./caesar dspttjohuifsvcjdpoabrkttds
# Shift 25: crossingtherubiconzaqjsscr

## nilai yang paling mendekati adalah ini
picoCTF{crossingtherubiconzaqjsscr}
```

# flag
picoCTF{crossingtherubiconzaqjsscr}