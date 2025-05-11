# Browser Forensic 9
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
extension id dengan icon salah satu vpn yang diinstal V.. ! \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini saya menggunakan DB Browser for SQLite untuk mempermudah proses pencarian.
- Saya membuka tabel yang berisi data URL, dan mencari entri yang mengandung extension Chrome. Dari hasil pencarian, saya menemukan salah satu URL yang mencurigakan:
  ![alt text](<images/Browser Forensic 9/image.png>)
- Kemudian saya buka URL tersebut, dan dari sana saya mengambil hanya bagian extension ID-nya saja:
  ![alt text](<images/Browser Forensic 9/image-1.png>)
- Setelah mendapatkan ID extension tersebut, saya menyusun flag dengan format berikut: **IDN_FLAG{majdfhpaihoncoakbjgbdhglocklcgno}**

## flag
IDN_FLAG{majdfhpaihoncoakbjgbdhglocklcgno}