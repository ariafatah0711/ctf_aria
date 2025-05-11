# Browser Forensic 10
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! (Filenya ada di pertanyaan pertama) \
Version vpn V.. yang diinstal oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Karena sebelumnya saya sudah mengetahui VPN apa saja yang terinstal, selanjutnya saya mencoba mencari tahu versi dari VPN tersebut dengan mengecek direktori Extensions.
- Saya menggunakan perintah berikut untuk melihat struktur folder hingga level 2: ```tree Extensions -L 2```
- Hasilnya sebagai berikut:
  ```bash
  Extensions
  ├── ghbmnnjooekpmoecnnnilnnbdlolhkhi
  │   └── 1.91.1_0
  ├── majdfhpaihoncoakbjgbdhglocklcgno
  │   └── 3.4.3_0
  ├── nmmhkkegccagdldgiimedpiccmgmieda
  │   └── 1.0.0.6_0
  ├── omghfjlpggmjjaagoclmmobgdodcjboh
  │   └── 3.90.4_0
  └── Temp
  ```
- Karena ID extension majdfhpaihoncoakbjgbdhglocklcgno sebelumnya sudah diketahui sebagai salah satu VPN, saya tinggal mencocokkannya. Dari struktur folder di atas, terlihat bahwa versi VPN tersebut adalah: ```3.4.3_0```

## flag
IDN_FLAG{3.4.3_0}