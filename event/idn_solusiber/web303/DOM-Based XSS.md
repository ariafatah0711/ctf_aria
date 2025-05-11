# DOM-Based XSS
## soal
-

## solve
- Pada tantangan XSS DOM ini, saya pertama-tama mencoba payload sederhana seperti:```<script>alert{'test'}</script``` namun tidak berhasil
- Namun, payload tersebut tidak berhasil. Selanjutnya, saya mencoba payload lain yang lebih umum digunakan: ```<img src="p" onerror="alert('test')">```
- Payload ini berhasil dijalankan, menandakan bahwa aplikasi rentan terhadap XSS berbasis DOM. Kemudian, saya mencoba mengecek apakah ada variabel bernama FLAG yang bisa diakses langsung lewat JavaScript, dengan payload: ```<img src="p" onerror="alert(FLAG)">```
  ![alt text](<images/DOM-Based XSS/image.png>)
- Hasilnya, muncul alert berisi string: ```27oFx9NE945YFuBYFshct2G4Mi3hmKpS7UTWS87yKMn```
- lalu saya mencoba mendecode dengan cyber chef dengan recipe **Magic** dan berhasil mendapatkan flagnya
  ![alt text](<images/DOM-Based XSS/image-1.png>)

## flag
IDN_CTF{dom_based_xss_executed}