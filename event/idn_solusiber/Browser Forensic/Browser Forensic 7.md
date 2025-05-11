# Browser Forensic 7
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
date_created pada email menggunakan tools DB Browser SQLite ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini kita diminta untuk mencari tanggal pembuatan email, dan karena sebelumnya kita sudah mengetahui alamat emailnya, langkah selanjutnya adalah mencari data terkait menggunakan DB Browser for SQLite.
- Biasanya, informasi pembuatan user/email tersimpan di dalam file Web Data, khususnya pada bagian autofill form.
- Saya pun membuka file Web Data menggunakan SQLite Browser:
  ![alt text](<images/Browser Forensic 7/image.png>)
- Setelah menelusuri datanya, saya menemukan timestamp yang mengindikasikan waktu pembuatan email. Saya kemudian mencoba langsung memasukkan flag dengan format: ```IDN_FLAG{1746250363}```

## flag
IDN_FLAG{1746250363]