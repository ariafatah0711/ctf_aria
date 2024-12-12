# soal
How about some hide and seek? \
Download this file here.

# hint
- How can you view the information about the picture?
- If something isn't in the expected form, maybe it deserves attention?

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/129/unknown.zip
unzip unknown.zip

file ukn_reality.jpg
# ukn_reality.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 4308x2875, components 3

exiftool ukn_reality.jpg
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==

echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYjMyMDQwYjh9Cg==" | base64 -d
# picoCTF{ME74D47A_HIDD3N_b32040b8}
```

# flag
picoCTF{ME74D47A_HIDD3N_b32040b8}