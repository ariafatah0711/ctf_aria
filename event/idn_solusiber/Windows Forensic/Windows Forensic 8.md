# Windows Forensic 8
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
SID Dari User Guest ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini kita diminta untuk mencari SUID dari user guest.
- Awalnya saya mencari di file USERS, namun tidak menemukan informasi SUID yang dimaksud. Setelah itu, saya mencoba menelusuri lokasi lain dan menemukan informasi yang relevan di path berikut: ```Accqution\Windows\System32\config\SAM\SAM\Domains\Builtin\Aliases```
  ![alt text](<images/Windows Forensic 8/image.png>)
- Di bagian ini, saya menemukan entri yang berkaitan dengan user guest:
  ![alt text](<images/Windows Forensic 8/image-1.png>)
- Setelah itu, saya submit nilai SUID yang ditemukan sebagai flag — dan flag tersebut berhasil.

## flag
IDN_FLAG{S-1-5-21-2412307826-2007293762-2764304457-501}