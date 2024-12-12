# soal
Someone's commits seems to be preventing the program from working. Who is it? \
You can download the challenge files here: \
challenge.zip

# hint
- In collaborative projects, many users can make many changes. How can you see the changes within one file?
- Read the chapter on Git from the picoPrimer here.
- You can use python3 <file>.py to try running the code, though you won't need to for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/159/challenge.zip
unzip challenge.zip
cd drop-in/

cat message.py
# print("Hello, World!"

git log | grep -v "important business work"
# commit 23e9d4ce78b3cea725992a0ce6f5eea0bf0bcdd4
# Author: picoCTF{@sk_th3_1nt3rn_81e716ff} <ops@picoctf.com>
# Date:   Tue Mar 12 00:07:15 2024 +0000

#    optimize file size of prod code

# commit 3ce5c692e2f9682a866c59ac1aeae38d35d19771
# Author: picoCTF <ops@picoctf.com>
# Date:   Tue Mar 12 00:07:15 2024 +0000

#     create top secret project

git shortlog
# picoCTF (501):
#       create top secret project
#       important business work
#       important business work
#       important business work

git shortlog -s -n
#    501  picoCTF
#      1  picoCTF{@sk_th3_1nt3rn_81e716ff}

## ternyata terdapat author yang bernama flag itu sendiri
# picoCTF{@sk_th3_1nt3rn_81e716ff}
```

# flag
picoCTF{@sk_th3_1nt3rn_81e716ff}