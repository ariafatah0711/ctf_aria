---
layout: level
level: 31
previous: ./level 30.html
next: ./level 32.html
---

# soal
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

# solve
```bash
workdir=$(mktemp -d)
cd $workdir

git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
# pass qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

cd repo
cat README.md
# just an epmty file... muahaha

git tag
# secret

git show secret
# fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

git show-ref
# acfc3c67816fc778c4aeb5893299451ca6d65a78 refs/heads/master
# acfc3c67816fc778c4aeb5893299451ca6d65a78 refs/remotes/origin/HEAD
# acfc3c67816fc778c4aeb5893299451ca6d65a78 refs/remotes/origin/master
# 84368f3a7ee06ac993ed579e34b8bd144afad351 refs/tags/secret

git cat-file -p "84368f3a7ee06ac993ed579e34b8bd144afad351" # hash
# fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy
```

# flag
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy