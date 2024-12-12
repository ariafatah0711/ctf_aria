# soal
Our flag printing service has started glitching! \
Additional details will be available after launching your challenge instance.

## launch istance
Our flag printing service has started glitching! \
$ nc saturn.picoctf.net 57434

# hint
- ASCII is one of the most common encodings used in programming
- We know that the glitch output is valid Python, somehow!
- Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

# solve
```bash
nc saturn.picoctf.net 57434
# 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
^C

python3
print('picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}')
# picoCTF{gl17ch_m3_n07_9c42a45d}
```

# flag
picoCTF{gl17ch_m3_n07_9c42a45d}