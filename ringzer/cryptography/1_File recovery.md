# soal
https://ringzer0ctf.com/files/e2c9757d48bd69a357a78223dd4a2bd1.zip \
MD5 sum: e2c9757d48bd69a357a78223dd4a2bd1

# solve
## use wget
```bash
wget https://ringzer0ctf.com/files/e2c9757d48bd69a357a78223dd4a2bd1.zip

md5sum e2c9757d48bd69a357a78223dd4a2bd1.zip
# a76b64cdbc90473d0d00aeffc0d46b99  e2c9757d48bd69a357a78223dd4a2bd1.zip

md5sum e2c9757d48bd69a357a78223dd4a2bd1.zip | grep e2c9757d48bd69a357a78223dd4a2bd1
# a76b64cdbc90473d0d00aeffc0d46b99  e2c9757d48bd69a357a78223dd4a2bd1.zip

## berbeda sumnya
cat e2c9757d48bd69a357a78223dd4a2bd1.zip
# 01001001 01100110 00100000 01111001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01100001 00100000 01100111 01100101 01101110 01110100 01101100 01100101 00100000 01101000 01100001 01100011
# ...

# if i decypct: 
echo "" | python3 -c "teks = input().split(); [print(chr(int(i, 2))) for i in teks]" | tr -d "\n"
# If you are a gentle hacker you are welcome to download files. If you are a fucking bot that scan the Internet using stupid heuristic rules that sucks then you are not welcome. Sincerely, Mr.Un1k0d3r
```

## manual install
```bash
find . -type f -exec md5sum {} \; | grep e2c9757d48bd69a357a78223dd4a2bd1
# e2c9757d48bd69a357a78223dd4a2bd1  ./manual/e2c9757d48bd69a357a78223dd4a2bd1.zip
# a76b64cdbc90473d0d00aeffc0d46b99  ./wget/e2c9757d48bd69a357a78223dd4a2bd1.zip

## terlihat disini dibagian download manual mendapatkan md5sum yang cocok

file manual/e2c9757d48bd69a357a78223dd4a2bd1.zip
# manual/e2c9757d48bd69a357a78223dd4a2bd1.zip: Zip archive data, at least v1.0 to extract, compression method=store
unzip manual/e2c9757d48bd69a357a78223dd4a2bd1.zip
ls flag/
# flag.enc  private.pem

## saya mencoba decrypt menggunakan openssl

cd flag
cat private.pem
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDFDxrLz/lBabo/JrRvKN47IRzUgm/LzG9zbn3g8HMnPIpy4ZOF
fhjblvb8iNeFMbUIDAT2QmsqDRJhHH7xUVfC6DiYB3YuKJC/RBIHzqlBsxWXI5DF
ikyS3yT6ThQap3JZEKE7fVXHHJmea4VrsRVhWG6ztoPYf+OfiMyzj0IV3QIDAQAB
AoGAX1QnSmGZ2yMijlpS/1Nt7nzeTY+sNZL4d4cELkUj799BusGVdAbET7aAVTp9
yFl7kiD+ZYNMBFO+iGwYnPUU1sPSlFcS1YNu2S+4ds2ym1VfZu2drTN5qUIGIm22
2mgyOG1CSx421Ns4X5qIexkQ1gOnqaBuD7Mi3D19c5mK66ECQQDlt99Jcw7Jh1Gd
TMy8cQ7EBI82YPedRP5SnAv0/sCIgcsBmbABO6WwCeS1BVjoicf+pPmIy3YkyiyO
8JIa9GJLAkEA25qwREClnm+2qIBRLal+pG8t7xZlEya+HrlX3ogThf/9GybfImzK
ZQagbom3sDmRTeu6PhDhu4XZS7D4gfIPdwJANlDrsupJrM0aNx9ZqZTx8NdDJZB3
+++8Urwi96Lk02IdJhu4yhHYc29jbIn/I7ywVT2c4wN4w+op7wJjCYyPUQJAaVEo
U7NFOlSNHwZa6DEvQSDowI7W7nZYG1f74gcUheEcu5bK0DGoZwbkjd6SL3uMSfhR
G07xUwOAEKLQq1ExRQJBAJouci7CVIbd8XqZEBaBAqIEVKCff+qHsHzoZo1ryog8
vIgevI9e/01CqyuKIRs9WmM+DU/QnZtLJHUqgkpSCag=
-----END RSA PRIVATE KEY-----

## karena rsa saya mencari di google cara decyprnya dan ternyata menggunakan openssl
openssl rsautl --decrypt -in flag.enc -inkey private.pem -out flag

cat flag
# FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

# flag
FLAG-vOAM5ZcReMNzJqOfxLauakHx