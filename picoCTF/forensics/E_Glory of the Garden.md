# soal
This garden contains more than it seems.

# hint
- What is a hex editor?

# solve
```bash
wget https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg

file garden.jpg
# garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3

exiftool garden.jpg
binwalk garden.jpg
# DECIMAL       HEXADECIMAL     DESCRIPTION
# --------------------------------------------------------------------------------
# 0             0x0             JPEG image data, JFIF standard 1.01
# 382           0x17E           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company

strings garden.jpg
# Here is a flag "picoCTF{more_than_m33ts_the_3y33dd2eEF5}"
```

# flag
picoCTF{more_than_m33ts_the_3y33dd2eEF5}