# Windows Forensic 1
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
Nama file yang menyimpan credential ? \
format flag : IDN_FLAG{Jawaban yang disoal} example : xxxxxxxx_xxx.xxx

## solve
- Di sini kita diminta untuk mencari nama file yang menyimpan credential.
- Saya menggunakan Registry Explorer sebagai alat bantu, lalu membuka file hive yang bernama **NTUSER.data**:
  ![alt text](<images/Windows Forensic 1/image.png>)
- Awalnya saya mencoba menelusuri registry secara manual, namun belum menemukan hasil yang jelas. Kemudian saya menemukan cara yang lebih cepat, yaitu dengan membuka tab di sebelah kanan yang berisi **Available Bookmarks:**
  ![alt text](<images/Windows Forensic 1/image-1.png>)
- Dari sana, saya menemukan file yang relevan dan mencoba submit dengan format: **IDN_FLAG{password_docs.txt}** dan berhasil

## flag
IDN_FLAG{password_docs.txt}