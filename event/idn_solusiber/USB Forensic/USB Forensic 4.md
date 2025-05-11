# USB Forensic 4
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Apa Disk ID yang dipakai hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Pada tantangan ini, kita diminta untuk mencari Disk ID yang digunakan oleh hacker.
- Untuk menyelesaikannya, saya menggunakan tool reglookup dan menjalankan perintah berikut: ```reglookup USBTOR.hiv | grep DiskId```
  ![alt text](<images/USB Forensic 4/image.png>)
- Dari hasil output, saya berhasil menemukan nilai Disk ID yang dimaksud.
- Kemudian, saya memasukkan flag dengan format: **IDN_FLAG{a4aaa1f8-27d0-11f0-a0ac-000c2979b63d}**

## flag
IDN_FLAG{a4aaa1f8-27d0-11f0-a0ac-000c2979b63d}