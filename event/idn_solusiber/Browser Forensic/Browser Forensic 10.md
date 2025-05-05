# Browser Forensic 10
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! (Filenya ada di pertanyaan pertama) \
Version vpn V.. yang diinstal oleh user ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini karena sebelumnya sudah mengetahui vpn apa yang di install disini saya mencoba untuk melihat version dengan melihat file **Extension**
  ```bash
  tree Extensions -L 2
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
- disini karena vpn yang sebeluumnya sudah ditemukan dan id extensionya **majdfhpaihoncoakbjgbdhglocklcgno**
- disini jika kita lihat versinya adalah **3.4.3_0**

## flag
IDN_FLAG{3.4.3_0}