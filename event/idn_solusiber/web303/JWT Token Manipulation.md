# JWT Token Manipulation
## soal
-

## solve
- disini terdapat web input jwt token, disini saya mencoba membuat jwt token di web [jwt.io](https://jwt.io/)
- lalu saya mencoba beberapa payload, dan ketika saya coba membuat jwt token dengan payload ```{"role":"admin"}``` 
  ![alt text](<images/JWT Token Manipulation/image.png>)
- lalu saya mencoba menyalin token tersebut ke web input jwt token, dan ternyata berhasil
  ![alt text](<images/JWT Token Manipulation/image-1.png>)
- lalu saya mendecode dengan cyberchef dengan recipe **Magic** dan berhasil mendapatkan flagnya
  ![alt text](<images/JWT Token Manipulation/image-2.png>)

## flag
IDN_CTF{jwt_token_manipulated}