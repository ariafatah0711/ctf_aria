# Browser Forensic 5
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !!\
(Filenya ada di pertanyaan pertama) \
Visit Duration di Website yang berkaitan dengan Persistence, Privilage Escalation, DLL Injection ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : XX:XX:XX.XXX

## solve
- disini saya membuka file yang history dengan **sqlitebrowser** lalu saya membuka file **History** dan mencari di **visits** karena kita harus mencari **visit duration** nya
- disini saya buka yang urls dulu
  ![alt text](<images/Browser Forensic 5/image.png>)
- terdapat 3 yang menurut saya sesuai lalu saya mencoba membuka di **visits** dan melihat **visit duration** nya
  ![alt text](<images/Browser Forensic 5/image-1.png>)
  ```bash
  2345343
  32509459
  2260442
  ```
- lalu disini saya menganalisa kemungkinan yang bisa aja berhasil dengan bantuan chat gpt
  ![alt text](<images/Browser Forensic 5/image-2.png>)
- lalu saya coba salah satu flagnya dan berhasil mendapatkan flagnya
  ```bash
  B → IDN_FLAG{00:00:32.509}
  A+B → IDN_FLAG{00:00:34.854}
  A+B+C → IDN_FLAG{00:00:37.155}
  B+C → IDN_FLAG{00:00:34.769}
  ```

## flag
IDN_FLAG{00:00:32.509}