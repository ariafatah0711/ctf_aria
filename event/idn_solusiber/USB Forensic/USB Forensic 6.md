# USB Forensic 6
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Nama File Yang ada di USB ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari file di USB yang ada di laptop hacker.
- saya sudah mencoba mencari di file **USBTOR.hiv** namun masih belum ketemu.
- setelah itu saya mencoba mencari di file lainya
  ![alt text](images/a/image-1.png)
- saya menemukan extension **.txt**, hanya saja nama filenya dalam bentuk binary.
- jadi saya mencoba cara lain dengan menggunakan tool regripper seperti
  ```bash
  regripper -r RecentDocs.hiv -f ntuser
  regripper -r NTUSER.DAT -f ntuser
  ``` 
- namun masih belum berhasil jadi saya meminta bantuan chat gpt dan berhasil mendapatkan nama filenya ``````
  ![alt text](images/a/image-2.png)
- dan ketika saya coba input flagnya berhasil dengan format seperti ini IDN_FLAG{4fu284428u5984-8308848.txt}

## flag
IDN_FLAG{4fu284428u5984-8308848.txt}