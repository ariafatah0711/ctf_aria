# Prototype Pollution
## soal
-

## solve
- Pada tantangan ini, tersedia sebuah web yang memungkinkan pengguna mengirimkan konfigurasi aplikasi melalui form berbasis JSON.
- Pertama, saya mencoba mengirimkan konfigurasi sesuai dengan contoh yang tersedia, yaitu: ```{"theme":"dark"}```
  ![alt text](<images/Prototype Pollution/image.png>)
- Namun, konfigurasi tersebut belum memberikan akses sebagai admin.
- Setelah itu, saya mencoba menyalin output konfigurasi yang dikembalikan oleh aplikasi, lalu memodifikasinya dengan menambahkan parameter admin dan secure seperti berikut: ```{"theme":"dark","secure":false,"admin":true}``` dan berhasil
  ![alt text](<images/Prototype Pollution/image-1.png>)
- Payload ini berhasil, dan saya memperoleh akses sebagai admin.
- Setelah berhasil, aplikasi menampilkan data terenkripsi. Saya menyalin data tersebut dan mendekodenya menggunakan CyberChef dengan recipe "Magic", dan berhasil mendapatkan flag dari tantangan ini.
  ![alt text](<images/Prototype Pollution/image-2.png>)

## flag
IDN_CTF{prototype_pollution_success}