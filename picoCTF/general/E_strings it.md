# soal
Can you find the flag in file without running it?

# hint
- [strings](https://linux.die.net/man/1/strings)

# solve
```bash
wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings

strings strings
# /lib64/ld-linux-x86-64.so.2
# __cxa_finalize
# ...

strings strings | grep flag
strings strings | grep pico
# picoCTF{5tRIng5_1T_d66c7bb7}
```

# flag
picoCTF{5tRIng5_1T_d66c7bb7}