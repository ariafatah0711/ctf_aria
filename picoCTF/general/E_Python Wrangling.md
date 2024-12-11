# soal
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

# hint
- Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py
- $ man python

# solve
```
wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py
wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt
wget https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en

ls
# ende.py  flag.txt.en  pw.txt

python3 ende.py
# Usage: ende.py (-e/-d) [file]

cat flag.txt.en
# gAAAAABgUAIWuksW6PU7W1WFXiBWkF2S8VhtL_5335iazHhuBnWloiyt3ZAFwR2zyuG7iZLSVPaQIZLTxgo-WXIk6Cnk7-KZm1g1qo_v1zDMK5wDocmVFxL0o5ae6OrB9VKdh3HerIsy

cat pw.txt
# dbd1bea4dbd1bea4dbd1bea4dbd1bea4

python3 ende.py -d flag.txt.en
# Please enter the password:dbd1bea4dbd1bea4dbd1bea4dbd1bea4
# picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```

# flag
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}