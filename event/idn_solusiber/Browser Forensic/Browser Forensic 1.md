# Browser Forensic 1
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
Tools apa yang di cari oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- pertama saya download dulu filenya, dan mencoba mencari tau browser forensic, dan karena saya masih agak bingung saya mencoba mencari tau di chat gpt. intinya kita harus cari tau tool yang di cari oleh user dari data browser ini
- nah pertama saya dikasih tau bahwa kita bisa mencari history browser di path ini **Browser/Acuatiotion/User Data/Default** 
  ```bash
  unzip Browser.zip
  cd Browser/Acuatiotion/User Data/Default
  ```
- lalu saya diberitahu gunakan tool sqlite3 untuk membaca file history karena dia menggunakan format sql
  ```bash
  sqlite3 History
  .tables # melihat daftar tables
  ```
- setelah itu saya mencoba membaca tabels seperti ```select * from urls;``` namun outputnya masih terlalu banyak
- jadi saya mencoba membaca dengan menggunakan seperti filtering dengan menggunakan ```where url like github``` karena biasanya tool gitu berada di repository github
  ```bash
  sqlite> SELECT * FROM urls WHERE url LIKE '%github%';
  28|https://lolbas-project.github.io/|LOLBAS|1|0|13390724280712417|0
  29|https://www.google.com/search?q=mimikatz+github&oq=mimikatz+github&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEAAYhgMYgAQYigUyDQgHEAAYhgMYgAQYigUyCggIEAAYgAQYogQyBwgJEAAY7wXSAQkxMDk5M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8|mimikatz github - Google Search|1|0|13390724292042433|0
  30|https://github.com/ParrotSec/mimikatz|GitHub - ParrotSec/mimikatz|1|0|13390724294298462|0
  ```
- disini saya menemukan bahwa user mencari tool mimikatz di github

## flag
IDN_FLAG{Mimikatz}