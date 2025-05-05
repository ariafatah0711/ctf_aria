# Browser Forensic 3
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
Streaming Website yang ditonton oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- melanjutkan soal sebelumnya kita disuruh mencari website streming yang ditonton oleh user
- disini saya menemukan beberapa web setelah melakukan pencarian dengan ini **SELECT url FROM urls;**
  ```bash
  https://www.netflix.com/
  https://www.netflix.com/id-en/
  ```
- lalu saya mencoba submit dengan format seperti **IDN_FLAG{netflix}**, **IDN_FLAG{Netflix}** namun masih belum berhasil dan ketika saya coba dengan **IDN_FLAG{https://www.netflix.com/}** itu berhasil

## flag
IDN_FLAG{https://www.netflix.com/}