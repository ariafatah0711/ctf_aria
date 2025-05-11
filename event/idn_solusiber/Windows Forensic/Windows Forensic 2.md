# Windows Forensic 2
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
file yang menyimpan credential, dibuka pada tanggal berapa ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : xxxx-xx-xx xx:xx:xx \
Auhtor: Aditya Firman

## solve
- Sekarang kita diminta untuk mencari tanggal terakhir file penyimpan credential dibuka.
- Karena sebelumnya kita sudah berhasil menemukan nama filenya, langkah selanjutnya cukup melihat tanggal akses terakhir dari file tersebut.
  ![alt text](<images/Windows Forensic 2/image.png>)
- Setelah mendapatkan tanggal yang dimaksud, saya langsung submit flagnya sesuai format yang diminta — dan ternyata berhasil.

## flag
IDN_FLAG{2025-05-03 07:16:29}