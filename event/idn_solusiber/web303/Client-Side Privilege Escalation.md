# Client-Side Privilege Escalation 
## soal
[website](https://ctf.solusiber.com/web_101/lab5/)

## solve
- Saat membuka web, saya melihat tampilan yang menampilkan informasi role saat ini, yaitu: ```Current role: guest```
- Sebagai guest, saya tidak memiliki akses untuk melihat protected content.
  ![alt text](<images/Client-Side Privilege Escalation/image.png>)
- Namun, dari deskripsi soal disebutkan kata kunci localStorage, sehingga saya mengecek isi localStorage melalui Developer Tools di browser.
- Di sana saya menemukan item bernama user_role dengan nilai "guest". Saya mengubah nilainya menjadi "admin" secara manual.
  ![alt text](<images/Client-Side Privilege Escalation/image-1.png>)
- Setelah saya refresh atau klik kembali tombol Show Protected Content, saya berhasil mendapatkan flag dari aplikasi.
  ![alt text](<images/Client-Side Privilege Escalation/image-2.png>)

## flag
FLAG{client_side_privilege_escalation}