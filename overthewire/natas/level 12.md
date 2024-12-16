---
layout: level
level: 12
previous: ./level 11.html
next: ./level 13.html
---

# soal
Username: natas12
URL:      http://natas12.natas.labs.overthewire.org

# solve
- login with cred natas12:yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB
- lalu disini ada sebuah form gambar jpg yang kalo kita lihat dari codenya namaa file tersebut akan dibuat secara acak dengan format jpeg
  ![alt text](docs/images/image-22.png)
- jadi saya mencoba membuat backdoor php
  ```php
  cat simple.php 
  <?php echo system($_GET['c']); ?>
  ```
- dan mencoba menguploadnya dan ketika saya coba benar saja filenya diganti menjadi extension jpeg dengan nama acak
- dan untungnya ketika saya cek di burp suite tidak terdapat encrypt apapun jadi saya mengubahnya
  ![alt text](docs/images/image-23.png)
  ![alt text](docs/images/image-24.png)
- namun pas di forward hanya extensionnya saja namun tidak apa apa karena kita cuma butuh extensionya 
  ![alt text](docs/images/image-25.png)
- dan ketika saya coba buka filenya dengan urlnya saya sudah mendapatkan RCE
  ![alt text](docs/images/image-26.png)
- dan saya hanya perlu mendapatkan file passnya
  ![alt text](docs/images/image-27.png)

# flag
trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC