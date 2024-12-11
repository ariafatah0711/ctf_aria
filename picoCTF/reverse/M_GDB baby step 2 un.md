# soal
Can you figure out what is in the eax register at the end of the main function? \
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. \
If the answer was 0x11 your flag would be picoCTF{17}. \
Debug this.

# hint
- You could calculate eax yourself, or you could set a breakpoint for after the calculcation and inspect eax to let the program do the heavy-lifting for you.

# solve
```bash
wget https://artifacts.picoctf.net/c/520/debugger0_b
chmod +x debugger0_b


```

# flag