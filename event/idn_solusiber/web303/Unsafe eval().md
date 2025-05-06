# Unsafe eval() 
## soal
-

## solve
eval('alert(FLAG)')

- disini terdapat web yang menggunakan eval() untuk mengeksekusi kode yang diinputkan oleh user.
- saya mencoba memasukan payload seperti ini ```1+1``` dia menghasilkan ```2```
  ![alt text](<images/Unsafe eval()/image.png>)
- lalu saya mencoba melakukan alert ke varibale FLAG seperti sebelumnya dan berhasil ```alert(FLAG)```
  ![alt text](<images/Unsafe eval()/image-1.png>)
  ```bash
  8K1iQbpVVMPdiYxaREW9wJvvCmBnKZnNn9VguPSy71veTjEc
  ```
- lalu saya melakukan decode dengan cyberchef recipe **Magic** nya dan berhasil mendapatkan flagnya
  ![alt text](<images/Unsafe eval()/image-2.png>)

## flag
IDN_CTF{you_used_eval_successfully}