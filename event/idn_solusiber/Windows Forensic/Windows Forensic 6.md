# Windows Forensic 6
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
Last Login Time dari User Cli.. ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : xxxx-xx-xx xx:xx:xx

## solve
- disini kita dirusuh mencari last login time dari user Cli..
- jika dilihat ada user client jadi usernya adalah client, dan karena yang di cari last login berarti yang ini
  ![alt text](<images/Windows Forensic 6/image.png>)
- namun ketika di input flagnya dengan format seperti ini **IDN_FLAG{2025-05-03 03.42.49}**, belum berhasil dan ternyata harus pake **:** untuk jam nya, dan setlah itu saya submit dan berhasil

## flag
IDN_FLAG{2025-05-03 03:42:49}