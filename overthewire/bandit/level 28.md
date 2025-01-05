---
layout: default
level: 28
name_file: level
---

{% include level-section.html %}

# soal
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo via the port 2220. \
The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

# solve
```bash
workdir=$(mktemp -d)
cd $workdir

git clone --help
# GIT URLS
#        In general, URLs contain information about the transport protocol, the address of the remote server, and the path to the repository. Depending on the transport protocol,
#        some of this information may be absent.
#        Git supports ssh, git, http, and https protocols (in addition, ftp and ftps can be used for fetching, but this is inefficient and deprecated; do not use them).
#        The native transport (i.e. git:// URL) does no authentication and should be used with caution on unsecured networks.

#        The following syntaxes may be used with them:
#        •   ssh://[user@]host.xz[:port]/path/to/repo.git/
#        •   git://host.xz[:port]/path/to/repo.git/
#        •   http[s]://host.xz[:port]/path/to/repo.git/
#       •   ftp[s]://host.xz[:port]/path/to/repo.git/

git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
# pass: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

ls
# repo

cat repo/README
# The password to the next level is: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

# flag
Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN