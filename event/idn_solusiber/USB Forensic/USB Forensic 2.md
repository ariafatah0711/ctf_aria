# USB Forensic 2
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
ClassGUID Pada USB Hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari ClassGUID pada USB Hacker.
- disini saya melihat hasil yang sebelumnya dan menemukan ClassGUID nya dengan perintah sebelumnya ```reglookup USBTOR.hiv | grep ClassGUID```
  ![alt text](<images/USB Forensic 2/image-1.png>)
- lalu tinggal input flagnya ```IDN_FLAG{4d36e967-e325-11ce-bfc1-08002be10318}```

## flag
IDN_FLAG{4d36e967-e325-11ce-bfc1-08002be10318}