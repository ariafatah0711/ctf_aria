# Timing Attack
## soal
- 

## solve
- Pada tantangan ini, terdapat sebuah web yang tampaknya rentan terhadap **timing attack**. Saya perhatikan bahwa ketika mengirimkan input satu per satu, **respons server menunjukkan perbedaan waktu (dalam milidetik)**, tergantung dari huruf yang saya kirimkan. 
- Saya mulai dengan mengirimkan satu karakter, dan ketika saya mencoba huruf ```p```, responsnya adalah ```1ms```, yang mengindikasikan bahwa huruf tersebut kemungkinan benar.
  ![alt text](<images/Timing Attack/image.png>)
- Saya kemudian melanjutkan dengan **menambahkan karakter satu per satu, menjadi pa, pas, dan seterusnya.** Dari pola respons yang konsisten, saya mencurigai bahwa password-nya adalah ```password```. Namun, input tersebut masih belum berhasil memberikan flag.
- Saya pun mencoba menambahkan beberapa angka setelah kata password, dan ketika saya menginputkan ```password123```, akhirnya saya berhasil mendapatkan respons yang berisi flag terenkripsi. ```NmMm6LByWzRL5zYUYocFN2qt1Lv7WDhkiLf6zqN2mVLuA```
  ![alt text](<images/Timing Attack/image-1.png>)
- Selanjutnya, saya menyalin string tersebut dan mendekodenya menggunakan CyberChef. Menggunakan recipe Magic, saya berhasil mendapatkan flag asli.
  ![alt text](<images/Timing Attack/image-2.png>)
  
## flag
IDN_CTF{timing_attack_successful}