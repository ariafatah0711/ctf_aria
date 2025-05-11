# Unsafe Deserialization
## soal
-

## solve
- Pada tantangan ini, terdapat sebuah web yang menerima input berupa JSON. Berdasarkan pengamatan awal, saya menduga bahwa aplikasi ini rentan terhadap **unsafe deserialization,** terutama karena tampaknya ada objek yang bisa dieksekusi.
- Karena sempat kebingungan, saya meminta bantuan dari ChatGPT dan juga mencoba memeriksa kode sumber melalui Inspect Element. Di situ, saya menemukan sebuah fungsi JavaScript berikut:
  ```js
  function unsafeDeserialize(data) {
      let parsed = JSON.parse(data);
      if (parsed && typeof parsed['run'] === 'string') {
      eval(parsed['run']);  // <-- 🔥 INI DIA VULNERABLE NYA
  }
      return parsed;
  }
  ```
- Dari kode di atas terlihat jelas bahwa nilai dari properti run dalam objek JSON akan dieksekusi langsung menggunakan eval() — ini merupakan titik kerentanan yang sangat berbahaya.
- Saya kemudian mencoba payload berikut: ```{"run": "alert(FLAG)"}```
- Payload ini berhasil dijalankan, dan menampilkan string FLAG dalam alert box.
  ![alt text](<images/Unsafe Deserialization/image.png>)
- Setelah itu, saya menyalin isi FLAG tersebut, mendekodenya menggunakan CyberChef, dan berhasil mendapatkan flag asli dari tantangan ini.
  ![alt text](<images/Unsafe Deserialization/image-1.png>)

## flag
IDN_CTF{unsafe_deserialization_executed}