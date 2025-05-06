# Prototype Pollution
## soal
-

## solve
- disini terdapat web yang terdapat submit json untuk mengubah configurasi app
- disini saya mencoba menginputkan yang ada di example config nya ```{"theme":"dark"}```
  ![alt text](<images/Prototype Pollution/image.png>)
- ternyata kita tidak dapet hak akses admin lalu saya mencoba untuk menyalin outputnya dan mengubah adminya menjadi true seperti ini payloadnya: ```{"theme":"dark","secure":false,"admin":true}``` dan berhasil
  ![alt text](<images/Prototype Pollution/image-1.png>)
- setelah itu saya mencoba mendecode dengan cyberchef dan berhasil mendapatkan flagnya
  ![alt text](<images/Prototype Pollution/image-2.png>)

## flag
IDN_CTF{prototype_pollution_success}