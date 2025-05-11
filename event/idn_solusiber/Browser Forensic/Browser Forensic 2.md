# Browser Forensic 2
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
Website apa yang dicari oleh user berkaitan dengan Teknik Persistence, Privilage Escalation, DLL Injection etc ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- Melanjutkan soal sebelumnya, kali ini kita diminta untuk mengidentifikasi tools yang berkaitan dengan teknik seperti Persistence, Privilege Escalation, DLL Injection, dan sejenisnya.
- Sebelumnya, saya sudah mendapatkan daftar URL yang diakses user dari hasil perintah: **SELECT url FROM urls WHERE url LIKE '%github%';** Berikut beberapa URL yang ditemukan:
  ```bash
  https://github.com/ParrotSec/mimikatz
  https://lolbas-project.github.io/
  https://www.google.com/search?q=mimikatz+github&oq=mimikatz+github&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEAAYhgMYgAQYigUyDQgHEAAYhgMYgAQYigUyCggIEAAYgAQYogQyBwgJEAAY7wXSAQkxMDk5M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
  ```
- Dari daftar tersebut, saya mencoba menganalisis mana dari URL tersebut yang berkaitan dengan teknik persistence, privilege escalation, atau DLL injection. Salah satu link yang mencurigakan dan relevan adalah: ```https://lolbas-project.github.io/```
- LOLBAS (Living Off The Land Binaries and Scripts) merupakan proyek yang mendokumentasikan bagaimana binary bawaan Windows dapat dimanfaatkan untuk berbagai teknik seperti privilege escalation, persistence, dan lainnya—yang sangat relevan dengan konteks soal.
- Awalnya saya mencoba memasukkan beberapa format flag seperti:
  - IDN_FLAG{lolbas}
  - IDN_FLAG{Lolbas}
  - IDN_FLAG{LOLBAS}
- Namun semuanya tidak berhasil.
- Akhirnya, saya mencoba menggunakan URL lengkap sebagai flag: ```IDN_FLAG{https://lolbas-project.github.io/}```

## flag
IDN_FLAG{https://lolbas-project.github.io/}