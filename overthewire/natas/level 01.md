---
layout: default
level: 1
name_file: level
---

{% include level-section.html %}

# soal
Username: natas1 \
URL:      http://natas1.natas.labs.overthewire.org

# solve
- login with cred natas1:0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
- inspect the web if cant right click
  - use shorcut dev tools "CTRL+SHIFT+I"
- or use view-source:<url>
- or use curl
  ```bash
  curl http://natas1.natas.labs.overthewire.org -u natas1:0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
  # <!--The password for natas2 is TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI -->
  ```

# flag
TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI