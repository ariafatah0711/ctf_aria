# Windows Forensic 8
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
SID Dari User Guest ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari SUID dari user guest, saya sudah mencari di file yang **USERS**, namun masih belum menemukan SUID nya
- dan saya mencoba mencari di tempat yang lain dan menemukan di path **E:\ctf_win\windows\Accqution\Windows\System32\config\SAM: SAM\Domains\Builtin\Aliases**
  ![alt text](<images/Windows Forensic 8/image.png>)
- lalu saya menemukan di bagian ini
  ![alt text](<images/Windows Forensic 8/image-1.png>)
- dan saya submit flagnya dan berhasil

## flag
IDN_FLAG{S-1-5-21-2412307826-2007293762-2764304457-501}