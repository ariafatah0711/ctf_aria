# Windows Forensic 6
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
Last Login Time dari User Cli.. ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : xxxx-xx-xx xx:xx:xx

## solve
- Di sini kita diminta untuk mencari last login time dari user yang namanya diawali dengan "Cli..".
- Setelah saya telusuri, terlihat bahwa user tersebut adalah "client", dan karena yang diminta adalah waktu login terakhir, maka saya fokus pada informasi last login:
  ![alt text](<images/Windows Forensic 6/image.png>)
- Awalnya saya mencoba submit flag dengan format: ```IDN_FLAG{2025-05-03 03.42.49}```
- Namun format tersebut belum berhasil. Setelah saya ubah dengan menggunakan titik dua (:) sebagai pemisah waktu, seperti ini: ```IDN_FLAG{2025-05-03 03:42:49}``` - Baru flag tersebut berhasil.

## flag
IDN_FLAG{2025-05-03 03:42:49}