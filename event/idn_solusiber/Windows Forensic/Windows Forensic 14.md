# Windows Forensic 14
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
GUID Dari Device DISK&VEN_TOSHIBA&PROD_TRANSMEMORY&REV_1.00 ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- saya menemukan lokasi GUID device disk di **SYSTEM**
- disini saya mencoba membuka tab **available** biar lebih mudah mencarinya
- lalu saya copy nama device nya setelah itu saya mencari manual, dan akhirnya saya menempukan pathnya
  ![alt text](<images/Windows Forensic 14/image.png>)

## flag
IDN_FLAG{eec5ad98-8080-425f-922a-dabf3de3f69a}