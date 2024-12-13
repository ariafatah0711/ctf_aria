# soal
There's an interesting script in the user's home directory \
The work computer is running SSH. \
We've been given a script which performs some basic calculations, explore the script and find a flag.

## launch istance
Hostname: saturn.picoctf.net \
Port:     63565 \
Username: picoplayer \
Password: password

# solve
```bash
ssh picoplayer@saturn.picoctf.net -p 63565
# picoplayer@saturn.picoctf.net's password:

ls
# useless
./useless
# Read the code first

man useless
# Authors
#      This script was designed and developed by Cylab Africa
#      picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}
```

# flag
picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_6194}