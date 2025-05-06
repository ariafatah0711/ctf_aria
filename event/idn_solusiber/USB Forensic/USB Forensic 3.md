# USB Forensic 3
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Apa Containder ID USB Yang dipakai Hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari Containder ID USB yang dipakai hacker
- saya mencoba dengan menggunakan perintah ```reglookup USBTOR.hiv | grep ContainerID```
  ![alt text](<images/USB Forensic 3/image.png>)
- setelah itu saya input flagnya dan berhasil **IDN_FLAG{11775948-7a76-52b3-9bc7-19cb3d487774}**

## flag
IDN_FLAG{11775948-7a76-52b3-9bc7-19cb3d487774}