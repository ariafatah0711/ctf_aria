# Windows Forensic 11
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
Buildlab pada Windows ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini kita diminta untuk mencari Build Lab pada Windows.
- Masih berada di path yang sama seperti sebelumnya: ```SOFTWARE\Microsoft\Windows NT\CurrentVersion```
- Saya mencari dan menemukan nilai BuildLab di dalam key tersebut.
  ![alt text](<images/Windows Forensic 11/image.png>)
- Setelah menemukannya, saya submit nilainya sebagai flag — dan flag tersebut berhasil.

## flag
IDN_FLAG{19041.vb_release.191206-1406}