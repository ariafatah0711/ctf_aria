---
layout: default
test_level1
name_file: level
---

{% include level-section.html %}

# soal
Leviathan’s levels are called leviathan0, leviathan1, … etc. and can be accessed on leviathan.labs.overthewire.org through SSH on port 2223.

To login to the first level use: \
Username: leviathan0 \
Password: leviathan0 \
Data for the levels can be found in the homedirectories. You can look at /etc/leviathan_pass for the various level passwords.

# solve
```bash
ssh leviathan0@leviathan.labs.overthewire.org -p 2223
# pass: leviathan0

ls -a
# .  ..  .backup  .bash_logout  .bashrc  .profile
cd .backup/

cat bookmarks.html | grep pass
# <DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 3QJ3TgzHDq" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

# flag
3QJ3TgzHDq