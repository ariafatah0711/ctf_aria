# soal
Run the runme.py script to get the flag. Download the script with your browser or with wget in the webshell. \
Download runme.py Python script

# hint
- If you have Python on your computer, you can download the script normally and run it. Otherwise, use the wget command in the webshell.
- To use wget in the webshell, first right click on the download link and select 'Copy Link' or 'Copy Link Address'
- Type everything after the dollar sign in the webshell: $ wget , then paste the link after the space after wget and press enter. This will download the script for you in the webshell so you can run it!
- Finally, to run the script, type everything after the dollar sign and then press enter: $ python3 runme.py You should have the flag now!

# solve
```bas
wget https://artifacts.picoctf.net/c/34/runme.py

cat runme.py
# #!/usr/bin/python3
# flag ='picoCTF{run_s4n1ty_run}'
# print(flag)

python3 runme.py
# picoCTF{run_s4n1ty_run}
```

# flag
picoCTF{run_s4n1ty_run}