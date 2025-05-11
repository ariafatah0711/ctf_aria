# Windows Forensic 5
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
User yang localgroupnya ada 2, yaitu ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Masih melanjutkan dari langkah sebelumnya, kali ini kita diminta untuk mencari user yang tergabung dalam 2 local group.
- Saya menelusuri data yang ada melalui Registry Explorer dan menemukan informasi user serta grup lokal yang terkait:
  ![alt text](<images/Windows Forensic 5/image.png>)
- Setelah mengidentifikasi user yang memenuhi kriteria, saya mencoba submit flagnya — dan flag tersebut berhasil.

## flag
IDN_FLAG{Geraldin}