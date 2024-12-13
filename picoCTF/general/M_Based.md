# soal
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. \
Can you get the flag from this program to prove you are on the way to becoming 1337? \
Connect with nc jupiter.challenges.picoctf.org 29956.

# hint
- I hear python can convert things.
- It might help to have multiple windows open.

# solve
```bash
nc jupiter.challenges.picoctf.org 29956
# Let us see how data is stored
# Please give the 01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111 as a word.
# you have 45 seconds.....
# Input:
colorado
# Please give me the  163 154 165 144 147 145 as a word.
# Input:
sludge
# Please give me the 6f76656e as a word.
# Input:
oven
# You've beaten the challenge
# Flag: picoCTF{learning_about_converting_values_b375bb16}

# 1 binary to ascii
| python3 -c "teks = input().split(); [print(chr(int(i, 2))) for i in teks]" | tr -d "\n"
# 2 octal to ascii
| python3 -c "teks = input().split(); [print(chr(int(i, 8))) for i in teks]" | tr -d "\n"
# 3 hex to ascii
| python3 -c "teks = input(); print(bytes.fromhex(teks).decode('ascii'))"
python2 -c "print(''.decode('hex'))"
```

## soal 1
```bash
echo "01100011 01101000 01100001 01101001 01110010" | tr " " "\n"
# 01100011
# ...

echo "a r i a" | python3 -c "print(input().split())"
# ['a', 'r', 'i', 'a']

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "print(input())"
# 01100011 01101000 01100001 01101001 01110010

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "print(input().split())"
# ['01100011', '01101000', '01100001', '01101001', '01110010']

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "teks = input().split(); print(teks)"
# ['01100011', '01101000', '01100001', '01101001', '01110010']

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "teks = input().split(); [print(i) for i in teks]"
# 01100011
# ...

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "teks = input().split(); [print(int(i, 2)) for i in teks]"
# 99
# 104

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "teks = input().split(); [print(chr(int(i, 2))) for i in teks]"
# c
# h
# 

echo "01100011 01101000 01100001 01101001 01110010" | python3 -c "teks = input().split(); [print(chr(int(i, 2))) for i in teks]" | tr -d "\n"
# chair
```

## soal 2
```bash
echo "141 156 151 155 141 164 151 157 156" | python3 -c "teks = input().split(); print(teks)"
# ['141', '156', '151', '155', '141', '164', '151', '157', '156']

echo "141 156 151 155 141 164 151 157 156" | python3 -c "teks = input().split(); [print(int(i, 8)) for i in teks]"
# 97
# 110

echo "141 156 151 155 141 164 151 157 156" | python3 -c "teks = input().split(); [print(chr(int(i, 8))) for i in teks]"
# a
# n
# ...

echo "141 156 151 155 141 164 151 157 156" | python3 -c "teks = input().split(); [print(chr(int(i, 8))) for i in teks]" | tr -d "\n"
# animation
```

## soal 3
```bash
echo "6f76656e" | python3 -c "teks = input(); print(teks)"
# 6f76656e

echo "6f76656e" | python3 -c "teks = input(); print(bytes.fromhex(teks))"
# b'oven'

echo "6f76656e" | python3 -c "teks = input(); print(bytes.fromhex(teks).decode('ascii'))"
# oven
```

# flag
picoCTF{learning_about_converting_values_b375bb16}