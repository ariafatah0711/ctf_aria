# soal
Find the flag in this picture.

# hint
- What does meta mean in the context of files?
- Ever heard of metadata?

# solve
```
wget https://jupiter.challenges.picoctf.org/static/916b07b4c87062c165ace1d3d31ef655/pico_img.png
exiftool pico_img.png
# Artist                          : picoCTF{s0_m3ta_d8944929}
```

# flag
picoCTF{s0_m3ta_d8944929}