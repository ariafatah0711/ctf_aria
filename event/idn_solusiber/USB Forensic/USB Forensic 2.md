# USB Forensic 2
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
ClassGUID Pada USB Hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Pada tantangan ini, kita diminta untuk mencari ClassGUID dari perangkat USB.
- Saya menggunakan tool reglookup untuk menganalisis file registry USBTOR.hiv. Dengan menjalankan perintah: ```reglookup USBTOR.hiv | grep ClassGUID```
  ![alt text](<images/USB Forensic 2/image-1.png>)
- Saya berhasil menemukan nilai ClassGUID yang dimaksud.
- Setelah mendapatkan nilainya, saya langsung mencoba memasukkan flag dengan format berikut: ```IDN_FLAG{4d36e967-e325-11ce-bfc1-08002be10318}```

## flag
IDN_FLAG{4d36e967-e325-11ce-bfc1-08002be10318}