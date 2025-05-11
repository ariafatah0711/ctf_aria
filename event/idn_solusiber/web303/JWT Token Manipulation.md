# JWT Token Manipulation
## soal
-

## solve
- Pada tantangan ini, tersedia sebuah web yang meminta input berupa JWT token.
- Saya mencoba membuat JWT token sendiri menggunakan situs [jwt.io](https://jwt.io/). Awalnya, saya bereksperimen dengan beberapa payload, dan akhirnya saya mencoba payload berikut: ```{"role": "admin"}```
  ![alt text](<images/JWT Token Manipulation/image.png>)
- Token yang dihasilkan kemudian saya salin dan masukkan ke dalam web pada kolom input JWT token.
- Ternyata, token tersebut diterima, dan saya berhasil mendapatkan output berupa data terenkripsi yang kemungkinan besar merupakan flag.
  ![alt text](<images/JWT Token Manipulation/image-1.png>)
- Saya menyalin data tersebut dan mendekodenya menggunakan CyberChef dengan recipe Magic, dan berhasil mendapatkan flag aslinya.
  ![alt text](<images/JWT Token Manipulation/image-2.png>)

## flag
IDN_CTF{jwt_token_manipulated}