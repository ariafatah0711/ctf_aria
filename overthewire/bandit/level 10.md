---
layout: default
level: 10
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

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