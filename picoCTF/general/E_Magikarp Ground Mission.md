# soal
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. \
Login via `ssh` as `ctf-player` with the password, `ee388b88` \
Additional details will be available after launching your challenge instance.

## launch istance
Challenge Endpoints \
SSH	ssh ctf-player@venus.picoctf.net -p 58700 \

# hint
- Finding a cheatsheet for bash would be really helpful!

# solve
```bash
ssh ctf-player@venus.picoctf.net -p 58700
# pass: ee388b88

## flag 1
ls
# 1of3.flag.txt  instructions-to-2of3.txt
cat 1of3.flag.txt
# picoCTF{xxsh_
cat instructions-to-2of3.txt
# Next, go to the root of all things, more succinctly `/`

## flag 2
ls
# 2of3.flag.txt  bin  boot  dev  etc  home  instructions-to-3of3.txt  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
cat 2of3.flag.txt
# 0ut_0f_\/\/4t3r_
cat instructions-to-3of3.txt
# Lastly, ctf-player, go home... more succinctly `~

## flag 3
cd /home/ctf-player/
ls
# 3of3.flag.txt  drop-in
cat 3of3.flag.txt
# 3ca613a1}
```

- gabungkan formatnya menjadi
  ```
  picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}
  ```

# flag
picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}