# Browser Forensic 1
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
Tools apa yang di cari oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Pertama-tama, saya mengunduh file yang diberikan, lalu mencoba memahami dasar dari browser forensics.
- Karena saya masih cukup bingung, saya meminta bantuan ChatGPT untuk memandu prosesnya. Inti dari tantangan ini adalah mencari tahu tool apa yang dicari oleh user melalui data browser.
- Saya diberitahu bahwa data history browser dapat ditemukan pada path: **Browser/Acuatiotion/User Data/Default** 
  ```bash
  unzip Browser.zip
  cd Browser/Acuatiotion/User Data/Default
  ```
- Kemudian saya mengekstrak file zip dan masuk ke direktori tersebut:
- Selanjutnya, saya diminta untuk menggunakan tool sqlite3, karena file history browser disimpan dalam format database SQLite. Berikut perintah yang saya gunakan:
  ```bash
  sqlite3 History
  .tables # melihat daftar tables
  ```
- Setelah melihat daftar tabel, saya mencoba membaca isi tabel urls: ```select * from urls;```
- Namun, hasilnya terlalu banyak. Untuk mempersempit pencarian, saya menggunakan filtering berdasarkan kata kunci github, karena umumnya tools open-source seperti yang dimaksud sering di-host di GitHub: ```SELECT * FROM urls WHERE url LIKE '%github%';```
- Dari hasil tersebut, saya menemukan beberapa entri penting, antara lain:
  ```bash
  sqlite> SELECT * FROM urls WHERE url LIKE '%github%';
  28|https://lolbas-project.github.io/|LOLBAS|1|0|13390724280712417|0
  29|https://www.google.com/search?q=mimikatz+github&oq=mimikatz+github&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEAAYhgMYgAQYigUyDQgHEAAYhgMYgAQYigUyCggIEAAYgAQYogQyBwgJEAAY7wXSAQkxMDk5M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8|mimikatz github - Google Search|1|0|13390724292042433|0
  30|https://github.com/ParrotSec/mimikatz|GitHub - ParrotSec/mimikatz|1|0|13390724294298462|0
  ```
- Dari sini terlihat jelas bahwa user sedang mencari tool bernama mimikatz di GitHub.

## flag
IDN_FLAG{Mimikatz}