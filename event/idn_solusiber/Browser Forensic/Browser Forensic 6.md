# Browser Forensic 6
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! (Filenya ada di pertanyaan pertama) \
Email yang digunakan pada browser ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini saya mencoba mencari email dari file Preferences
  ```bash
  grep -i '"email"' Preferences
  # "email":"ghxyssforunfun@gmail.com",
  ```
  ![alt text](<images/Browser Forensic 6/image.png>)

## flag
IDN_FLAG{ghxyssforunfun@gmail.com}