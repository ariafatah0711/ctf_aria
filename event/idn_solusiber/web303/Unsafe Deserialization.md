# Unsafe Deserialization
## soal
-

## solve
- disini terdapat web load json lagi, namun terdapat unsave Deserialization, sepertinya ada object yang bisa di exploit
- karena saya agak kebingungan saya minta bantuan chat gpt dan mencoba menyalin script yang di inspect element dan ternyata terdapat sebuah **unsafe eval** yang bisa dicoba
  ```bash
  function unsafeDeserialize(data) {
      let parsed = JSON.parse(data);
      if (parsed && typeof parsed['run'] === 'string') {
      eval(parsed['run']);  // <-- 🔥 INI DIA VULNERABLE NYA
  }
      return parsed;
  }
  ```
- lalu saya coba menggunakan payyload run dengan payload ```{"run": "alert(FLAG)"}```
  ![alt text](<images/Unsafe Deserialization/image.png>)
  
- lalu saya coba decode dan berhasil mendapatkan flagnya
  ![alt text](<images/Unsafe Deserialization/image-1.png>)

## flag
IDN_CTF{unsafe_deserialization_executed}