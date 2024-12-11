# soal
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

# hint
- This program will only work in the webshell or another Linux computer.
- To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm
- Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm
- -h and --help are the most common arguments to give to programs to get more information from them!
- Not every program implements help features like -h and --help.

# solve
```bash
wget https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm
chmod +x warm

./warm
# Hello user! Pass me a -h to learn what I can do!

./warm -h
# Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```

# flag
picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}