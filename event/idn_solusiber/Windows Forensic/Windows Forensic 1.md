# Windows Forensic 1
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
Nama file yang menyimpan credential ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : xxxxxxxx_xxx.xxx

## solve
- disini saya kita disuruh mencari nama file yang menyimpan credential.
- saya menggunakan tools registrey explorer dan saya mencoba membuka hive yang filenya **NTUSER.data**
  ![alt text](<images/Windows Forensic 1/image.png>)
- saya sudah mencari namunmasih belum ketemu dan saya menemukan metode agar lebih cepat yaitu dengan membuka tab yang di kananya yang avaible bookmarks
  ![alt text](<images/Windows Forensic 1/image-1.png>)
- lalu saya submit flagnya dengan format **IDN_FLAG{password_docs.txt}** dan berhasil

## flag
IDN_FLAG{password_docs.txt}