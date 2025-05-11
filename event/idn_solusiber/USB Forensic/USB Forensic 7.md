# USB Forensic 7
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Direktory Yang ada di usb ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : *:\directory

## solved
- Pada tantangan ini, kita diminta untuk mencari nama direktori yang terdapat di USB.
- Sebelumnya, saya mencoba menyelesaikannya di Kali Linux. Namun, kali ini saya mencobanya di Windows menggunakan Registry Explorer. Saya berhasil menemukan nama folder yang dimaksud.
  ![alt text](<images/USB Forensic 7/image-2.png>)
- Awalnya, saya kesulitan dalam menebak format flag yang benar, karena dalam petunjuk flag terdapat karakter seperti *:. Saya mencoba beberapa format, dan akhirnya berhasil menemukan format yang tepat, yaitu: ```IDN_FLAG{E:\-04893u42=b5u024u50u}```
- Untuk membantu proses analisis, saya juga menggunakan tools ShellBags, yang menurut saya sangat membantu dalam melihat jalur folder (path) dengan lebih mudah.
  ![alt text](<images/USB Forensic 7/image-1.png>)
- Dari situ, saya menemukan path mount folder USB di file USRCLASS.dat, yang memperkuat informasi sebelumnya.
  ![alt text](<images/USB Forensic 7/image.png>)

## flag
IDN_FLAG{E:\\-04893u42=b5u024u50u}