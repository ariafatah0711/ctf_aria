# soal
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. \
Can you find the flag? You'll have 1000 possibilities and only 10 guesses. \
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. \
Practicing the fundamentals manually might help you in the future when you have to write your own tools! \
You can download the challenge files here: \
challenge.zip

Additional details will be available after launching your challenge instance.

## launch istance
ssh -p 64844 ctf-player@atlas.picoctf.net \
Using the password 83dcefb7. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

# hint
- Have you ever played hot or cold? Binary search is a bit like that.
- You have a very limited number of guesses. Try larger jumps between numbers!
- The program will randomly choose a new number each time you connect. You can always try again, but you should start your binary search over from the beginning - try around 500. Can you think of why?

# solve
```bash
wget https://artifacts.picoctf.net/c_atlas/4/challenge.zip
unzip challenge.zip

cd home/ctf-player/drop-in
cat guessing_game.sh
#            #!/bin/bash
#            # Generate a random number between 1 and 1000
#            target=$(( (RANDOM % 1000) + 1 ))

## disini bisa kita lihat bahwa ini adalah game tebak angka random
## yang dibatasi 10 kali (max_guest)

## disini saya langsung mencoba dengan memulai di angka 500 untuk mengetahui posisi mana yang pas
ssh -p 64844 ctf-player@atlas.picoctf.net
# ctf-player@atlas.picoctf.net's password:
# Welcome to the Binary Search Game!
# I'm thinking of a number between 1 and 1000.
Enter your guess: 500
# Lower! Try again.
Enter your guess: 250
# Lower! Try again.
Enter your guess: 125
# Higher! Try again.
Enter your guess: 175
# Higher! Try again.
Enter your guess: 200
# Lower! Try again.
Enter your guess: 185
# Higher! Try again.
Enter your guess: 190
# Lower! Try again.
Enter your guess: 187
# Congratulations! You guessed the correct number: 187
# Here's your flag: picoCTF{g00d_gu355_ee8225d0}
# Connection to atlas.picoctf.net closed.
```

# flag
picoCTF{g00d_gu355_ee8225d0}