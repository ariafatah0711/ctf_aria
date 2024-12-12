# soal
You will find the flag after decrypting this file \
Download the encrypted flag here.

# hint
- Sometimes rotation is right

# solve
```bash
# wget https://artifacts.picoctf.net/c/386/encrypted.txt
cat encrypted.txt
# xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}

# kurasa ini rot 13
https://raw.githubusercontent.com/ariafatah0711/ctf_aria/refs/heads/main/tool/caesar
chmod +x caesar

./caesar "xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}"
# Shift 17: ohbnBSE{q0szs1nm_c3bqxos3c_4b71e5a0}
# Shift 18: picoCTF{r0tat1on_d3crypt3d_4c71f5b0}
```

# flag
picoCTF{r0tat1on_d3crypt3d_4c71f5b0}