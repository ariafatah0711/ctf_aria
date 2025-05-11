# Unsafe eval() 
## soal
-

## solve
- Saya mencoba memasukkan payload sederhana seperti  ```1+1```, dan hasilnya berhasil dieksekusi, yakni menghasilkan output ```2```.
  ![alt text](<images/Unsafe eval()/image.png>)
- Dari situ saya menyimpulkan bahwa input dievaluasi secara langsung. Kemudian saya mencoba menampilkan nilai dari variabel FLAG menggunakan payload: ```alert(FLAG)```
  ![alt text](<images/Unsafe eval()/image-1.png>)
- Payload tersebut berhasil dijalankan, dan saya mendapatkan output berikut: ```8K1iQbpVVMPdiYxaREW9wJvvCmBnKZnNn9VguPSy71veTjEc```
- String tersebut saya decode menggunakan CyberChef dengan recipe “Magic”, dan hasilnya adalah flag.
  ![alt text](<images/Unsafe eval()/image-2.png>)

## flag
IDN_CTF{you_used_eval_successfully}