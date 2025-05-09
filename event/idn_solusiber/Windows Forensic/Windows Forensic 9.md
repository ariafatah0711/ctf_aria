# Windows Forensic 9
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
CurrentBuild pada Windows ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari Current Build pada Windows
- jadi saya mencoba membuka file yang **SOFTWARE**
  ![alt text](<images/Windows Forensic 9/image.png>)
- lalu saya membuka path yang ini untuk melihat informasi windows **SOFTWARE: Microsoft\Windows NT\CurrentVersion**
  ![alt text](<images/Windows Forensic 9/image-1.png>)
- dan disini saya menemukan current buildnya
  ![alt text](<images/Windows Forensic 9/image-2.png>)
- dan saya coba submit flagnya dan berhasil

## flag
IDN_FLAG{19045}