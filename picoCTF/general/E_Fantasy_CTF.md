# soal
lay this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF. \
Connect to the program with netcat: $ nc verbal-sleep.picoctf.net 61243

# hint
- When a choice is presented like [a/b/c], choose one, for example: c and then press Enter.

# solve
```bash
nc verbal-sleep.picoctf.net 61243
# A
# A
# A
# A -> regis
# A -> play game

# echo -e "A\nA\nA\nA\nA\An" | nc verbal-sleep.picoctf.net 61243
```

# flag
picoCTF{m1113n1um_3d1710n_8dcbda00}