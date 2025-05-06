# USB Forensic 5
## soal
ada hacker, physical acces ke laptop.. bantuin dong ! \
(Filenya ada di pertanyaan pertama) \
Apa Serial ID USB Yang dipakai Hacker ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- disini kita disuruh mencari Serial ID namun saya tidak menemukan dengan grep
- dan disini saya mencoba input yang ada di sebelum properties, sepertinya ini serial idnya
  ![alt text](images/a/image.png)
- dan setelah saya input ternyata berhasil **IDN_FLAG{XRVZQBFR&0}**

## flag
IDN_FLAG{XRVZQBFR&0}