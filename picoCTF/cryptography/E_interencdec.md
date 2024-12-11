# soal
Can you get the real meaning from this file. \
Download the file here.

# hint
- Engaging in various decoding processes is of utmost importance

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/109/enc_flag
cat enc_flag
# YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg==

echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyMHdNakV5TnpVNGZRPT0nCg==" | base64 -d
# b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ=='

echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX20wMjEyNzU4fQ==" | base64 -d
# wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}

## decyrpt with caesar cipher
## if u want use tool online or u can use my tool
wget https://raw.githubusercontent.com/ariafatah0711/ctf_aria/refs/heads/main/tool/caesar
chmod +x caesar

./caesar "wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}"
# Shift 1: xqkwKBN{kimaiz_l3kz9xb3l_n0212758}
# Shift 18: ohbnBSE{bzdrzq_c3bq9os3c_e0212758}
# Shift 19: picoCTF{caesar_d3cr9pt3d_f0212758}
# Shift 20: qjdpDUG{dbftbs_e3ds9qu3e_g0212758}
```

# flag
picoCTF{caesar_d3cr9pt3d_f0212758}