# Browser Forensic 3
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
Streaming Website yang ditonton oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Melanjutkan soal sebelumnya, kita diminta untuk mencari website streaming yang dikunjungi oleh user. Saya mulai dengan menjalankan query: ```SELECT url FROM urls;```
- Dari hasilnya, saya menemukan beberapa URL:
  ```bash
  https://www.netflix.com/
  https://www.netflix.com/id-en/
  ```
- Awalnya, saya mencoba submit flag dengan format seperti ```IDN_FLAG{netflix}``` dan ```IDN_FLAG{Netflix}```, tetapi hasilnya salah. Lalu saya mencoba submit menggunakan format lengkap URL, yaitu ```IDN_FLAG{https://www.netflix.com/}```, dan ternyata itu yang benar.

## flag
IDN_FLAG{https://www.netflix.com/}