---
layout: level
level: 30
previous: ./level 29.html
next: ./level 31.html
---

# soal
There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

# solve
```bash
workdir=$(mktemp -d)
cd $workdir

git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
# pass: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

cd repo
git show
# commit 6ac7796430c0f39290a0e29a4d32e5126544b022 (HEAD -> master, origin/master, origin/HEAD, list)
# Author: Ben Dover <noone@overthewire.org>
# Date:   Thu Sep 19 07:08:41 2024 +0000

#     fix username

# diff --git a/README.md b/README.md
# index 2da2f39..1af21d3 100644
# --- a/README.md
# +++ b/README.md
# @@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.

 ## credentials

# -- username: bandit29
# +- username: bandit30
# - password: <no passwords in production!>

git branch
# * master

git branch -a
# * master
#  remotes/origin/HEAD -> origin/master
#  remotes/origin/dev
#  remotes/origin/master
#  remotes/origin/sploits-dev

######### remotes/origin/ (sama aja dengan yang remotes/origin/master karena dia symbolink)

######### remotes/origin/dev (terdapat password)
git checkout remotes/origin/dev
git branch
# * (HEAD detached at origin/dev)
#  master

git show
# -- password: <no passwords in production!>
# +- password: qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

######### remotes/origin/sploits-dev (kosong isinya)
git checkout remotes/origin/sploits-dev
git show
# ++ b/exploits/horde5.md
# @@ -0,0 +1 @@
# +
```

# flag
qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL