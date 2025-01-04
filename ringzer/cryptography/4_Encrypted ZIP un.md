# soal
wierd.zip and flag.zip apparently have the same password. We also found a unzipped version of wierd.txt \
MD5 sum: 0e7e17b0a3b18dbce02ad55c6cf868ae

# setup
```bash
wget --header="Cookie: PHPSESSID=<value>" https://ringzer0ctf.com/files/0e7e17b0a3b18dbce02ad55c6cf868ae.zip
md5sum 0e7e17b0a3b18dbce02ad55c6cf868ae.zip | grep 0e7e17b0a3b18dbce02ad55c6cf868ae
# 0e7e17b0a3b18dbce02ad55c6cf868ae  0e7e17b0a3b18dbce02ad55c6cf868ae.zip
```

# solve
```bash
unzip 0e7e17b0a3b18dbce02ad55c6cf868ae.zip

wget https://github.com/keyunluo/pkcrack/raw/refs/heads/master/bin/pkcrack
chmod +x pkcrack

zip w.zip weird.txt 
#  adding: weird.txt (deflated 100%)
/pkcrack -C weird.zip -c weird.txt -P w.zip -p weird.txt
```

# flag
