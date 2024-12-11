---
layout: level
level: 6
previous: ./level 05.html
next: ./level 07.html
---

# soal
Username: natas6
URL:      http://natas6.natas.labs.overthewire.org

# solve
- use cred natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned
- disini setelah saya login saya menemukan sebuah form untuk input secret
- dan disini juga terdapat viwe-source untuk melihat codenya
  ![alt text](docs/images/image-6.png)
- disini jika kita lihat terdapat sebuah path inclue untuk mengimport "include "includes/secret.inc";"
  ![alt text](docs/images/image-7.png)
- karena saya sudah mendapatkan includenya saya hanya perlu untuk memasukan kode secret tersebut ke dalam form tadi
  - dan ini flagnya: "Access granted. The password for natas7 is bmg8SvU1LizuWjx3y7xkNERkHxGre0GS"

# flag
bmg8SvU1LizuWjx3y7xkNERkHxGre0GS