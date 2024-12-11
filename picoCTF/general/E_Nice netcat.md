# soal
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 43239, but it doesn't speak English...

# hint
- You can practice using netcat with this picoGym problem: [what's a netcat](https://play.picoctf.org/practice/challenge/34)
- You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

# solve
```bash
nc mercury.picoctf.net 43239
# 112
# 105

cat in.txt | tr "\n" " "
# 112  105  99  111  67  84  70  123  103  48  48  100  95  107  49  116  116  121  33  95  110  49  99  51  95  107  49  116  116  121  33  95  55  99  48  56  50  49  102  53  125  10
cat in.txt | tr "\n" " " | tr -d " "
# 11210599111678470123103484810095107491161161213395110499951951074911611612133955599485650491025312510

## namun saatt dilanjutkan tidak berhaasil
## jadi saya mencoba cara lain

awk '{printf "%c", $0}' in.txt
# picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}

python3 -c "print(''.join(chr(int(line)) for line in open('in.txt')))"
# picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}
```

# flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5}