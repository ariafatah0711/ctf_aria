# Browser Forensic 8
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
url favicon, di website yang dicari oleh user ? ( tidak berkaitan dengan hacker !!! ) \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini saya mencoba mencari favicon untuk icon web yang pernah dikunjungi dan harus mencari yang bukan website berkaitan hacker
- disini saya menggunakan tool **sqlitebrowser** dan membuka file Favicons
  ![alt text](<images/Browser Forensic 8/image.png>)
- atau kita bisa gunakan 
  ```bash
  sqlite3 Favicons
  SQLite version 3.46.1 2024-08-13 09:16:08
  Enter ".help" for usage hints.
  sqlite> select * from Favicons;
  1|https://ssl.gstatic.com/chrome/webstore/images/icon_48px.png|1
  2|https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2023.ico|1
  3|https://www.muslima.com/lp/paid-search/terra-assets/images/favicon-8b7d9ccfa1-3.ico|1
  4|https://github.githubassets.com/favicons/favicon.svg|1
  5|https://www.google.com/favicon.ico|1
  6|https://lolbas-project.github.io/assets/favicon.png|1
  ```
  ![alt text](<images/Browser Forensic 8/image-1.png>)
- lalu saya mencoba salah satu itu yang menurut saya tidak berkaitan dengan hacking dan berhasil mendapatkan flagnya

## flag
IDN_FLAG{https://www.muslima.com/lp/paid-search/terra-assets/images/favicon-8b7d9ccfa1-3.ico}