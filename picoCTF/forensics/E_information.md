# soal
Files can always be changed in a secret way. Can you find the flag? cat.jpg

# hint
- Look at the details of the file
- Make sure to submit the flag as picoCTF{XXXXX}

# solve
```bash
wget https://mercury.picoctf.net/static/149ab4b27d16922142a1e8381677d76f/cat.jpg

file cat.jpg
# cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
binwalk cat.jpg
stat cat.jpg

exiftool cat.jpg
# Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
# Copyright Notice                : PicoCTF
# Application Record Version      : 4
# XMP Toolkit                     : Image::ExifTool 10.80
# License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
# Rights                          : PicoCTF

echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
picoCTF{the_m3tadata_1s_modified}
```

# flag
picoCTF{the_m3tadata_1s_modified}