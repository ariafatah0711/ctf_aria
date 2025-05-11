# Windows Forensic 10
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
DisplayVersion pada Windows ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini kita diminta untuk mencari Display Version dari Windows.
- Karena masih berada di lokasi yang sama seperti sebelumnya, yaitu:  ```SOFTWARE\Microsoft\Windows NT\CurrentVersion```
- Saya langsung mencari nilai DisplayVersion di dalam key tersebut.
  ![alt text](<images/Windows Forensic 10/image.png>)
- Setelah menemukannya, saya submit nilainya sebagai flag — dan flag tersebut berhasil.

## flag
IDN_FLAG{22H2}