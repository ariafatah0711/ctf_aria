# soal
What was I last working on? I remember writing a note to help me remember... \
You can download the challenge files here: \
challenge.zip

# hint
- The cat command will let you read a file, but that won't help you here!
- Read the chapter on Git from the picoPrimer here.
- When committing a file with git, a message can (and should) be included.

# solve
```
wget https://artifacts.picoctf.net/c_titan/160/challenge.zip
unzip challenge.zip
cd drop-in/

cat message.txt
# This is what I was working on, but I'd need to look at my commit history to know why...

git log
# commit 89d296ef533525a1378529be66b22d6a2c01e530 (HEAD -> master)
# Author: picoCTF <ops@picoctf.com>
# Date:   Tue Mar 12 00:07:22 2024 +0000

#     picoCTF{t1m3m@ch1n3_186cd7d7}
```

# flag
picoCTF{t1m3m@ch1n3_186cd7d7}