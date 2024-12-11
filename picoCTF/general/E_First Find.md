# soal
Unzip this archive and find the file named 'uber-secret.txt' \
Download zip file

# solve
```bash
wget https://artifacts.picoctf.net/c/501/files.zip
unzip files.zip
cd files/

find . -type f -name "uber-secret.txt"
# ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt

cat ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
picoCTF{f1nd_15_f457_ab443fd1}
```

# flag
picoCTF{f1nd_15_f457_ab443fd1}