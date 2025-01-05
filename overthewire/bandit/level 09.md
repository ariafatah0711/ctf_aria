---
layout: default
level: 9
name_file: level
---

{% include level-section.html %}

# soal
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

# solve
```bash
sort data.txt | uniq -u
```

# flag
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM