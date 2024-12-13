# soal
How to automate tasks to run at intervals on linux servers? \
Additional details will be available after launching your challenge instance.

## launch istance
Server: saturn.picoctf.net \
Port: 58081 \
Username: picoplayer \ 
Password: bLgSMmbY6X

# solve
```bash
ssh picoplayer@saturn.picoctf.net -p 58081
# picoplayer@saturn.picoctf.net's password: bLgSMmbY6X

crontab -l
#  no crontab for picoplayer

cd /etc/cron.d
ls
# e2scrub_all

cat /etc/crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}
```

# flag
picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}