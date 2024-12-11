# soal
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

# hint
- Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

# solve
```bash
ipython3 -c "0x70" # DEC
# Out[1]: 112

ipython3 -c "chr(0x70)" # char
# Out[1]: 'p'
```

# flag
picoCTF{p}