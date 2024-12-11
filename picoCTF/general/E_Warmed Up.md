# soal
What is 0x3D (base 16) in decimal (base 10)?

# hint
- Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

# solve
- base16(hexdecimal) ke base10 (decimal)
  ```
  0x3D => 0011 1101
  00111110 => 32 + 16 + 8 + 4 + 1 => 61
  ```
- atau gunakan tool online
  - https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=3D
  - dan masukan 0x3D
- atau gunakan python
  ```bash
  ipython3

  int("0x3D", 16)
  Out[1]: 61
  ```

# flag
picoCTF{61}