# Browser Forensic 5
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !!\
(Filenya ada di pertanyaan pertama) \
Visit Duration di Website yang berkaitan dengan Persistence, Privilage Escalation, DLL Injection ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : XX:XX:XX.XXX

## solve
- Di sini saya membuka file riwayat (history) menggunakan DB Browser for SQLite, lalu saya membuka file History dan mencari pada tabel visits, karena kita diminta mencari visit duration-nya.
- Pertama, saya buka tabel urls terlebih dahulu:
  ![alt text](<images/Browser Forensic 5/image.png>)
- Terdapat tiga URL yang menurut saya relevan. Setelah itu, saya membuka tabel visits dan mencocokkannya untuk melihat nilai visit_duration:
  ![alt text](<images/Browser Forensic 5/image-1.png>)
- Hasilnya ada tiga nilai durasi:
  - 2345343
  - 32509459
  - 2260442
- Selanjutnya, saya menganalisis kemungkinan kombinasi durasi yang mungkin digunakan sebagai flag. Dengan bantuan ChatGPT, saya mencoba beberapa kemungkinan konversi durasi dalam format waktu:
  ![alt text](<images/Browser Forensic 5/image-2.png>)
  ```bash
  B → IDN_FLAG{00:00:32.509}
  A+B → IDN_FLAG{00:00:34.854}
  A+B+C → IDN_FLAG{00:00:37.155}
  B+C → IDN_FLAG{00:00:34.769}
  ```
- lalu saya coba salah satu flagnya dan berhasil mendapatkan flagnya

## flag
IDN_FLAG{00:00:32.509}