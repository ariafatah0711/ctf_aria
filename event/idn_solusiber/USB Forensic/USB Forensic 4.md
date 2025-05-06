# USB Forensic 4
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Apa Disk ID yang dipakai hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari Disk ID yang digunakan oleh Hacker
- saya mencoba dengan menggunakan perintah ```reglookup USBTOR.hiv | grep DiskId```
  ![alt text](<images/USB Forensic 4/image.png>)
- lalu saya submit flag nya yang berformat seperti ini **IDN_FLAG{a4aaa1f8-27d0-11f0-a0ac-000c2979b63d}**

## flag
IDN_FLAG{a4aaa1f8-27d0-11f0-a0ac-000c2979b63d}