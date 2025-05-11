# Windows Forensic 9
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
CurrentBuild pada Windows ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini kita diminta untuk mencari Current Build pada Windows.
- Untuk itu, saya membuka file **SOFTWARE** menggunakan Registry Explorer:
  ![alt text](<images/Windows Forensic 9/image.png>)
- Kemudian saya menavigasi ke path berikut untuk melihat informasi versi Windows: ```SOFTWARE\Microsoft\Windows NT\CurrentVersion```
  ![alt text](<images/Windows Forensic 9/image-1.png>)
- Di dalam path tersebut, saya menemukan nilai **CurrentBuild:**
  ![alt text](<images/Windows Forensic 9/image-2.png>)
- Setelah itu, saya submit nilainya sebagai flag — dan flag tersebut berhasil.

## flag
IDN_FLAG{19045}