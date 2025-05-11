# USB Forensic 3
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Apa Containder ID USB Yang dipakai Hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Pada tantangan ini, kita diminta untuk mencari Container ID dari USB yang digunakan oleh hacker.
- Saya menggunakan tool reglookup dan menjalankan perintah berikut untuk mencari nilai ContainerID: ```reglookup USBTOR.hiv | grep ContainerID```
  ![alt text](<images/USB Forensic 3/image.png>)
- Perintah tersebut berhasil menampilkan nilai ContainerID yang diperlukan.
- Setelah itu, saya memasukkan flag dengan format: **IDN_FLAG{11775948-7a76-52b3-9bc7-19cb3d487774}**

## flag
IDN_FLAG{11775948-7a76-52b3-9bc7-19cb3d487774}