# Windows Forensic 3
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
User yang dibuat pada tanggal 2025-05-03 07:04:43, Username nya ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini saya menggunakan Registry Explorer dan memuat **file SAM** yang berasal dari file **AD1**, yang sebelumnya telah diekstrak menggunakan **FTK Imager.**
  ![alt text](<images/Windows Forensic 3/image.png>)
- Selanjutnya, saya membuka path berikut: ```Accqution\Windows\System32\config\SAM\SAM\Domains\Account\Users```
  ![alt text](<images/Windows Forensic 3/image-1.png>)
- Setelah menelusuri data di path tersebut, saya mencoba submit flag berdasarkan informasi yang ditemukan — dan flag tersebut berhasil.

## flag
IDN_FLAG{Geraldin}