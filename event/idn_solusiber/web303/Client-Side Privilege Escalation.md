# Client-Side Privilege Escalation 
## soal
[website](https://ctf.solusiber.com/web_101/lab5/)

## solve
- ketika dibuka webnya terdapat tampilan seperti ini dan ada current role namun disini rolenya masih guest, dan tidak mendapatkan akses
  ![alt text](<images/Client-Side Privilege Escalation/image.png>)
- di deskripsi terdapat kata localstorage disini saya mengubah value localstorage yang user_role dari guest menjadi admin
  ![alt text](<images/Client-Side Privilege Escalation/image-1.png>)
- ketika saya coba show protected content disitu saya berhasil mendapatkan flagnya
  ![alt text](<images/Client-Side Privilege Escalation/image-2.png>)

## flag
FLAG{client_side_privilege_escalation}