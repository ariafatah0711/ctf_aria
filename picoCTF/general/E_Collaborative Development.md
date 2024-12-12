# soal
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? \
You can download the challenge files here: \
challenge.zip

# hint
- git branch -a will let you see available branches
- How can file 'diffs' be brought to the main branch? Don't forget to git config!
- Merge conflicts can be tricky! Try a text editor like nano, emacs, or vim.

# solve
```bash
wget https://artifacts.picoctf.net/c_titan/178/challenge.zip
unzip challenge.zip
cd drop-in/

cat flag.py
# print("Printing the flag...")

git branch -a
#   0a
#   feature/part-1
#   feature/part-2
#   feature/part-3
# * main

git checkout feature/part-1
# Switched to branch 'feature/part-1'

cat flag.py
# print("Printing the flag...")
# print("picoCTF{t3@mw0rk_", end='')

git checkout feature/part-2
# Switched to branch 'feature/part-2'

cat flag.py
# print("Printing the flag...")
# print("m@k3s_th3_dr3@m_", end='')

git checkout feature/part-3
# Switched to branch 'feature/part-3'

cat flag.py
# print("Printing the flag...")
# print("w0rk_6c06cec1}")

## lalu saya hanya perlu menggabungkan flagnya
# picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}
```

# flag
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}