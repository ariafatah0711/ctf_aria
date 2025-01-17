---
layout: default
level: 10
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

# ssh
```bash
sshpass -p "4CKMh1JI91bUIZZPXDqGanal4xvAg0JM" ssh -o StrictHostKeyChecking=no bandit9@bandit.labs.overthewire.org -p 2220
```

# solve
```bash
strings data.txt | grep =
# }========== the
# p\l=
# ;c<Q=.dEXU!
# 3JprD========== passwordi
# qC(=
# ~fDV3========== is
# 7=oc
# zP=
# ~de=
# 3k=fQ
# ~o=0
# 69}=
# %"=Y
# =tZ~07
# D9========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
# N=~[!N
# zA=?0j
```

# flag
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey