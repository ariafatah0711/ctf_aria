---
layout: level
level: 29
previous: ./level 28.html
next: ./level 30.html
---

# soal
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

# solve
```bash
workdir=$(mktemp -d)
cd $workdir

git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
# pass: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

cd repo

cat README.md
# # Bandit Notes
# Some notes for level29 of bandit.

# ## credentials

# - username: bandit29
# - password: xxxxxxxxxx

git log
# commit 817e303aa6c2b207ea043c7bba1bb7575dc4ea73 (HEAD -> master, origin/master, origin/HEAD)
# Author: Morla Porla <morla@overthewire.org>
# Date:   Thu Sep 19 07:08:39 2024 +0000

#     fix info leak

# commit 3621de89d8eac9d3b64302bfb2dc67e9a566decd
# Author: Morla Porla <morla@overthewire.org>
# Date:   Thu Sep 19 07:08:39 2024 +0000

#     add missing data

# commit 0622b73250502618babac3d174724bb303c32182
# Author: Ben Dover <noone@overthewire.org>
# Date:   Thu Sep 19 07:08:39 2024 +0000

#     initial commit of README.md

git show 0622b73250502618 # initial commit of README.md
# +- username: bandit29
# +- password: <TBD>

git show 3621de89d8eac9 # add missing data
# -- password: <TBD>
# +- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
```

# flag
4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7