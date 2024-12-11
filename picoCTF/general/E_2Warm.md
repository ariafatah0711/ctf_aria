# soal
Can you convert the number 42 (base 10) to binary (base 2)?

# hint
- Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.

# solve
- base10 (decimal) to base2 (binary)
  ```
  42 => 00101010
  # diambil 6 huruf karena tidak perlu semuanya
  ```
- with python3
  ```bash
  bin(42)
  # Out[1]: '0b101010'
  ```
- tool online
  - https://www.rapidtables.com/convert/number/decimal-to-binary.html?x=42

# flag
picoCTF{00101100}