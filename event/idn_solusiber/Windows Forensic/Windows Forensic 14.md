# Windows Forensic 14
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
GUID Dari Device DISK&VEN_TOSHIBA&PROD_TRANSMEMORY&REV_1.00 ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Saya menemukan lokasi GUID dari device disk di bagian **SYSTEM.**
- Untuk mempermudah pencarian, saya membuka tab **Available.**
-  Setelah itu, saya menyalin nama device-nya, lalu mencarinya secara manual. Akhirnya, saya berhasil menemukan path-nya.
  ![alt text](<images/Windows Forensic 14/image.png>)
- Setelah menemukannya, saya submit nilainya sebagai flag — dan flag tersebut berhasil.

## flag
IDN_FLAG{eec5ad98-8080-425f-922a-dabf3de3f69a}