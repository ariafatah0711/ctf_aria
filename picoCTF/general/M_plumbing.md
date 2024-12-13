# soal
Sometimes you need to handle process data outside of a file. \
Can you find a way to keep the output from this program and search for the flag? \
Connect to jupiter.challenges.picoctf.org 7480.

# hint
- Remember the flag format is picoCTF{XXXX}
- What's a pipe? No not that kind of pipe... This kind

# solve
```bash
nc jupiter.challenges.picoctf.org 7480
# Again, I really don't think this is a flag
# I don't think this is a flag either

nc jupiter.challenges.picoctf.org 7480 | grep pico
# picoCTF{digital_plumb3r_06e9d954}
```

# flag
picoCTF{digital_plumb3r_06e9d954}