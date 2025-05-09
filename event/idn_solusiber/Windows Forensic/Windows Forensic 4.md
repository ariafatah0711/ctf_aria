# Windows Forensic 4
## soal
Ceritanya, udh ambil hivenya.. mount, trus cari beberapa informasi tambahan lainya !! \
(Filenya ada di pertanyaan pertama) \
User yang dibuat pada tanggal 2025-05-03 07:05:03, Username nya ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Di sini saya menggunakan tools **Registry Explorer** dan mencoba memuat file **SAM** yang berasal dari file **AD1** yang sebelumnya telah diekstrak menggunakan **FTK Imager**.
  ![alt text](<images/Windows Forensic 4/image.png>)
- lalu saya mencoba membuka path **E:\ctf_win\windows\Accqution\Windows\System32\config\SAM: SAM\Domains\Account\Users**
  ![alt text](<images/Windows Forensic 4/image-1.png>)
- dan saya mencoba submit flagnya dan berhasil

## flag
IDN_FLAG{Jon}