# soal
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: Addadshashanammu.zip

# hint
- After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

# solve
```bash
wget https://mercury.picoctf.net/static/fe16c756149cfa85f23e73cd9dbd6a25/Addadshashanammu.zip

unzip Addadshashanammu.zip
cd Addadshashanammu/
tree
# .
# └── Almurbalarammi
#     └── Ashalmimilkala
#         └── Assurnabitashpi
#             └── Maelkashishi
#                 └── Onnissiralis
#                     └── Ularradallaku
#                         └── fang-of-haynekhtnamet

strings Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet | grep pico
# *ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}
```

# flag
picoCTF{l3v3l_up!_t4k3_4_r35t!_76266e38}