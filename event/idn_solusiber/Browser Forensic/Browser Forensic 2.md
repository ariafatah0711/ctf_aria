# Browser Forensic 2
## soal
Ada Volation yang dilakukan oleh user di satu laptop, coba bantu forensic browsernya dong !! \
(Filenya ada di pertanyaan pertama) \
Website apa yang dicari oleh user berkaitan dengan Teknik Persistence, Privilage Escalation, DLL Injection etc ? \
format flag : IDN_FLAG{Jawaban yang disoal}

## solve
- melanjutkan soal sebelumnya karena sebelumnya saya menemukan beberapa tool github dan saat ini saya disuruh mencari tools yang berkaitan dengan Teknik Persistence, Privilage Escalation, DLL Injection etc
- ini adalah hasil dari command **SELECT url FROM urls WHERE url LIKE '%github%';** urls yang sebelumnya
  ```bash
  https://github.com/ParrotSec/mimikatz
  https://lolbas-project.github.io/
  https://www.google.com/search?q=mimikatz+github&oq=mimikatz+github&gs_lcrp=EgZjaHJvbWUqDQgAEAAYkQIYgAQYigUyDQgAEAAYkQIYgAQYigUyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyDQgGEAAYhgMYgAQYigUyDQgHEAAYhgMYgAQYigUyCggIEAAYgAQYogQyBwgJEAAY7wXSAQkxMDk5M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
  ```
- lalu saya mencoba memasukan flag seperti **IDN_FLAG{lolbas}**, **IDN_FLAG{Lolbas}**, **IDN_FLAG{LOLBAS}**, dan masih belum berhasil
- saya juga sudah mencoba beberapa format flag lagi dan ternyata berhasil ketika saya memasukan flag dengan urlnya **IDN_FLAG{https://lolbas-project.github.io/}**

## flag
IDN_FLAG{https://lolbas-project.github.io/}