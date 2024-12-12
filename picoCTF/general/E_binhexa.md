# soal
How well can you perfom basic binary operations? \
Additional details will be available after launching your challenge instance.

## launch istance
How well can you perfom basic binary operations? \
Start searching for the flag here nc titan.picoctf.net 56437

# solve
```bash
nc titan.picoctf.net 56437
# Welcome to the Binary Challenge!"
# Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.
# Binary Number 1: 11001101
# Binary Number 2: 00010010

# Question 1/6:
# Operation 1: '+'
# Perform the operation on Binary Number 1&2.
Enter the binary result: 11011111
# Correct!

# Question 2/6:
# Operation 2: '|'
# Perform the operation on Binary Number 1&2.
Enter the binary result: 11011111
# Correct!

# Question 3/6:
# Operation 3: '&'
# Perform the operation on Binary Number 1&2.
Enter the binary result: 00000000
# Correct!

# Question 4/6:
# Operation 4: '>>'
# Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 00001001
# Correct!

# Question 5/6:
# Operation 5: '*'
# Perform the operation on Binary Number 1&2.
Enter the binary result: 111001101010
# Correct!

# Question 6/6:
# Operation 6: '<<'
# Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 110011010
# Correct!

Enter the results of the last operation in hexadecimal: 19A

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}

## question 1
In [7]: int("11001101", 2)
Out[7]: 205

In [8]: int("00010010", 2)
Out[8]: 18

In [11]: bin(int("11001101", 2) + int("00010010", 2))
Out[11]: '0b11011111'

## question 4
## di pertnyaan ke 4 kita disuruh mengeser binary yang nomer 2 sebanyak 1 bytes
## 00010010 => 0 + 00010010 -
##         =>     00001001

## question 5
In [12]: bin(int("11001101", 2) * int("00010010", 2))
Out[12]: '0b111001101010'

## question 6
## di question terakhir kita disuruh untuk menggeser binary ke kiri sebnyak 1 bytes
## 11001101 => 11001101 + 0 
##          => 110011010

## last
## disini kita disuruh convert hasil quest ke 6 menjadi hexdecimal
# 110011010
## kita perlu mengubahnya menjadi kelipatah 4 bit
# 1 1001 1010
# 000 + 1 1001 1010
# 000110011010
## 0001 1001 1010
## 1 9 A
## 19A
```

# flag
picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}