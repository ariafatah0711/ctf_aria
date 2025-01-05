---
layout: default
level: 32
name_file: level
---

{% include level-section.html %}

# soal
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

# solve
```bash
workdir=$(mktemp -d)
cd $workdir

git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
# pass: fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

cd repo
cat README.md
# This time your task is to push a file to the remote repository.

# Details:
#     File name: key.txt
#     Content: 'May I come in?'
#     Branch: master

## namun ketika saya baca lagi ternyata di README.md ini adalah intruksi jadi saya mengikutinya
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
# pass: fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
echo May I come in? > key.txt
echo "" > .gitignore

git add .
git commit -m "add"

git push
# remote: Well done! Here is the password for the next level:
# remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
```

## trash try
```bash
git show
# diff --git a/.gitignore b/.gitignore
# new file mode 100644
# index 0000000..2211df6
# --- /dev/null
# +++ b/.gitignore
# @@ -0,0 +1 @@
# +*.txt

## restore file commit
git fsck --lost-found
# Checking objects: 100% (4/4), done.

ls
# git-diagnostics-2024-12-10-1734.zip  README.md

# host
scp -P 2220 bandit31@bandit.labs.overthewire.org:/tmp/tmp.yFR4EEtgL3/repo/git-diagnostics-2024-12-10-1734.zip .
unzip git-diagnostics-2024-12-10-1734.zip

ls
# git-diagnostics-2024-12-10-1734.zip  packs-local.txt diagnostics.log  objects-local.txt
```

# flag
3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K