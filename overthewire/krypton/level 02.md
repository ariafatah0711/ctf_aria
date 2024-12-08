# soal
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. \
It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. \
This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

# solve
```bash
ssh krypton1@krypton.labs.overthewire.org -p 2231 
#                       _                     _              
#                      | | ___ __ _   _ _ __ | |_ ___  _ __  
#                      | |/ / '__| | | | '_ \| __/ _ \| '_ \ 
#                      |   <| |  | |_| | |_) | || (_) | | | |
#                      |_|\_\_|   \__, | .__/ \__\___/|_| |_|
#                                 |___/|_|                   

#                       This is an OverTheWire game server. 
#             More information on http://www.overthewire.org/wargames

# krypton1@krypton.labs.overthewire.org's password:

cd /krypton/krypton1
cat krypton2 
# YRIRY GJB CNFFJBEQ EBGGRA

echo "YRIRY GJB CNFFJBEQ EBGGRA" | tr '[N-ZA-M]' '[A-Z]'                   
# LEVEL TWO PASSWORD ROTTEN
```

## ROT 13
- caesar chiper shift 13 / ROT 13

# flag
ROTTEN