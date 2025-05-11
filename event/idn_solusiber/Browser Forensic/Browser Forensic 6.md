# Browser Forensic 6
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! (Filenya ada di pertanyaan pertama) \
Email yang digunakan pada browser ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini saya mencoba mencari email yang mungkin tersimpan di dalam file Preferences. Saya menggunakan perintah berikut untuk melakukan pencarian: ```grep -i '"email"' Preferences```
- Dari hasilnya, ditemukan entri sebagai berikut: ```"email":"ghxyssforunfun@gmail.com"```
  ![alt text](<images/Browser Forensic 6/image.png>)
- Dengan ini, saya berhasil menemukan email yang digunakan oleh user dari file konfigurasi browser tersebut.

## flag
IDN_FLAG{ghxyssforunfun@gmail.com}