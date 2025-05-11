# Browser Forensic 8
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
url favicon, di website yang dicari oleh user ? ( tidak berkaitan dengan hacker !!! ) \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini saya diminta untuk mencari favicon dari website yang pernah dikunjungi, dengan syarat favicon tersebut tidak berasal dari situs yang berkaitan dengan hacking.
- Saya menggunakan DB Browser for SQLite dan membuka file Favicons:
  ![alt text](<images/Browser Forensic 8/image.png>)
- Alternatifnya, kita juga bisa menggunakan command-line SQLite: ```sqlite3 Favicons```
- Setelah masuk, saya menjalankan query: ```SELECT * FROM Favicons;```
- Hasilnya menampilkan beberapa entri favicon:
  ```
  1|https://ssl.gstatic.com/chrome/webstore/images/icon_48px.png|1
  2|https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2023.ico|1
  3|https://www.muslima.com/lp/paid-search/terra-assets/images/favicon-8b7d9ccfa1-3.ico|1
  4|https://github.githubassets.com/favicons/favicon.svg|1
  5|https://www.google.com/favicon.ico|1
  6|https://lolbas-project.github.io/assets/favicon.png|1
  ```
  ![alt text](<images/Browser Forensic 8/image-1.png>)
- Dari daftar tersebut, saya menganalisis dan memilih salah satu URL favicon yang menurut saya tidak berkaitan dengan aktivitas hacking. Setelah mencoba submit sebagai flag, ternyata berhasil dan saya mendapatkan flag yang benar.

## flag
IDN_FLAG{https://www.muslima.com/lp/paid-search/terra-assets/images/favicon-8b7d9ccfa1-3.ico}