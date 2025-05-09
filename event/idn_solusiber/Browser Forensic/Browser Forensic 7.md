# Browser Forensic 7
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
date_created pada email menggunakan tools DB Browser SQLite ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari tanggal pembuatan email menggunakan tools DB Browser SQLite karena kita sebelumnya sudah mengetahui emailnya
- dan biasanya untuk pembuatan user berada di **Web Data → untuk autofill form, termasuk email**
- lalu saya menggunakan tool **sqlitebrowser** dan membuka file **Web Data**
  ![alt text](<images/Browser Forensic 7/image.png>)
- dan saya langsung aja menginputkan flagnya dengan format IDN_FLAG{1746250363}

## flag
IDN_FLAG{1746250363]