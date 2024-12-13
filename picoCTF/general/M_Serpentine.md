# soal
Find the flag in the Python script! \
Download Python script

# hint
- Try running the script and see what happens
- In the webshell, try examining the script with a text editor like nano
- To exit nano, press Ctrl and x and follow the on-screen prompts.
- The str_xor function does not need to be reverse engineered for this challenge.

# solve
```bash
wget https://artifacts.picoctf.net/c/35/serpentine.py

python3 serpentine.py
# a) Print encouragement
# b) Print flag
# c) Quit

# What would you like to do? (a/b/c) b
# Oops! I must have misplaced the print_flag function! Check my source code!

## jika saya lihat pada kodenya terdapat sebuahh function menampilkan flag hanya saja tidak dimasukan di if statment
# def print_flag():
#   flag = str_xor(flag_enc, 'enkidu')
#   print(flag)

## jadi saya coba masukan pada if statementnya
# elif choice == 'b':
#       print_flag()
#      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')

python3 serpentine.py
# What would you like to do? (a/b/c) b
# picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
```

# flag
picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}