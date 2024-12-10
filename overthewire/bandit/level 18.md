---
layout: level
level: 18
previous: ./level 17.html
next: ./level 19.html
---

# soal
There are 2 files in the homedirectory: passwords.old and passwords.new. \
The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new \

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

# solve
```bash
diff passwords.old passwords.new 
# 42c42
# < ktfgBvpMzWKR5ENj26IbLGSblgUG9CzB
# ---
# > x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

cat passwords.new | grep "x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO" -n
# 42:x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
cat passwords.new -n | grep 42
# 42  x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

# flag
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO