# soal
I accidentally wrote the flag down. Good thing I deleted it! \
You download the challenge files here: \
challenge.zip

# hint
- Version control can help you recover files if you change or lose them!
- Read the chapter on Git from the picoPrimer here
- You can 'checkout' commits to see the files inside them

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/77/challenge.zip
unzip challenge.zip
cd drop-in/

cat message.txt
# TOP SECRET

git log
# commit e1237df82d2e69f62dd53279abc1c8aeb66f6d64 (HEAD -> master)
# Author: picoCTF <ops@picoctf.com>
# Date:   Sat Mar 9 21:10:14 2024 +0000

#     remove sensitive info

# commit 3d5ec8a26ee7b092a1760fea18f384c35e435139
# Author: picoCTF <ops@picoctf.com>
# Date:   Sat Mar 9 21:10:14 2024 +0000
#     create flag

git show 3d5ec8a26ee
# +picoCTF{s@n1t1z3_30e86d36}

git show
# -picoCTF{s@n1t1z3_30e86d36}
# +TOP SECRET
```

# flag
picoCTF{s@n1t1z3_30e86d36}