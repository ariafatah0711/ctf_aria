---
layout: default
level: 7
name_file: level
---

{% include level-section.html %}

# soal
Hopefully by now its obvious that encryption using repeating keys is a bad idea. Frequency analysis can destroy repeating/fixed key substitution crypto.

A feature of good crypto is random ciphertext. A good cipher must not reveal any clues about the plaintext. Since natural language plaintext (in this case, English) contains patterns, it is left up to the encryption key or the encryption algorithm to add the ‘randomness’.

Modern ciphers are similar to older plain substitution ciphers, but improve the ‘random’ nature of the key.

An example of an older cipher using a complex, random, large key is a vigniere using a key of the same size of the plaintext. For example, imagine you and your confident have agreed on a key using the book ‘A Tale of Two Cities’ as your key, in 256 byte blocks.

The cipher works as such:

Each plaintext message is broken into 256 byte blocks. For each block of plaintext, a corresponding 256 byte block from the book is used as the key, starting from the first chapter, and progressing. No part of the book is ever re-used as key. The use of a key of the same length as the plaintext, and only using it once is called a “One Time Pad”.

Look in the krypton6 directory. You will find a file called ‘plain1’, a 256 byte block. You will also see a file ‘key1’, the first 256 bytes of ‘A Tale of Two Cities’. The file ‘cipher1’ is the cipher text of plain1. As you can see (and try) it is very difficult to break the cipher without the key knowledge.

If the encryption is truly random letters, and only used once, then it is impossible to break. A truly random “One Time Pad” key cannot be broken. Consider intercepting a ciphertext message of 1000 bytes. One could brute force for the key, but due to the random key nature, you would produce every single valid 1000 letter plaintext as well. Who is to know which is the real plaintext?!?

Choosing keys that are the same size as the plaintext is impractical. Therefore, other methods must be used to obscure ciphertext against frequency analysis in a simple substitution cipher. The impracticality of an ‘infinite’ key means that the randomness, or entropy, of the encryption is introduced via the method.

We have seen the method of ‘substitution’. Even in modern crypto, substitution is a valid technique. Another technique is ‘transposition’, or swapping of bytes.

Modern ciphers break into two types; symmetric and asymmetric.

Symmetric ciphers come in two flavours: block and stream.

Until now, we have been playing with classical ciphers, approximating ‘block’ ciphers. A block cipher is done in fixed size blocks (suprise!). For example, in the previous paragraphs we discussed breaking text and keys into 256 byte blocks, and working on those blocks. Block ciphers use a fixed key to perform substituion and transposition ciphers on each block discretely.

Its time to employ a stream cipher. A stream cipher attempts to create an on-the-fly ‘random’ keystream to encrypt the incoming plaintext one byte at a time. Typically, the ‘random’ key byte is xor’d with the plaintext to produce the ciphertext. If the random keystream can be replicated at the recieving end, then a further xor will produce the plaintext once again.

From this example forward, we will be working with bytes, not ASCII text, so a hex editor/dumper like hexdump is a necessity. Now is the right time to start to learn to use tools like cryptool.

In this example, the keyfile is in your directory, however it is not readable by you. The binary ‘encrypt6’ is also available. It will read the keyfile and encrypt any message you desire, using the key AND a ‘random’ number. You get to perform a ‘known ciphertext’ attack by introducing plaintext of your choice. The challenge here is not simple, but the ‘random’ number generator is weak.

As stated, it is now that we suggest you begin to use public tools, like cryptool, to help in your analysis. You will most likely need a hint to get going. See ‘HINT1’ if you need a kicktstart.

If you have further difficulty, there is a hint in ‘HINT2’.

The password for level 7 (krypton7) is encrypted with ‘encrypt6’.

Good Luck!

# ssh
```bash
sshpass -p "RANDOM" ssh -o StrictHostKeyChecking=no krypton6@krypton.labs.overthewire.org -p 2231

# scp
# sshpass -p "RANDOM" scp -R -P 2231 krypton6@krypton.labs.overthewire.org:/krypton/krypton6/* krypton6
```

# solve
```bash
cd /krypton/krypton6

workdir=$(mktemp -d)
cd $workdir
ln -s /krypton/krypton6/keyfile.dat

chmod 777 -R .

# example encrypt
echo "ARIAFATAHARIAFATAH" > plain.txt
/krypton/krypton6/encrypt6 plain.txt cipher
cat cipher
# EZKTIGRIFZBBHSSBRM

xxd plain.txt # binary

xxd -b plain.txt # binear
xxd -b cipher # binear 
```

## tabble
```bash
ABCDEFGHIJKLMNOPQRSTUVWXYZ
01234567890123456789012345

P = 01000001 01010010 01001001 01000001 01000110 01000001 01010100 01000001 01001000 01000001 01010010 01001001 01000001 01000110 01000001 01010100 01000001 01001000
C = 01000101 01011010 01001011 01010100 01001001 01000111 01010010 01001001 01000110 01011010 01000010 01000010 01001000 01010011 01010011 01000010 01010010 01001101
K = 

# A => E
P = 01000001
C = 01000101
K = 00000100 => 4 => E

# R => Z
P = 01010010
C = 01011010
K = 00001000 => 8 => I

## namun cara ini lama ada 1 cara biar enak dengan membuat sebuah plain text yaitu AAAAAA
# karena apapaun yang di xor dengan A akan menghasilkan key itu sendiri
p = 00000000
k = 00000001 => 1 => b
c = 00000001 => 1 => b

p = 00000000
k = 00001001 => 9 => j
c = 00001001 => 9 => j
```

## solve with the key AAAA...
```bash
python3 -c "print('A'*100)" > a
/krypton/krypton6/encrypt6 a cipher
cat cipher 
# EICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZKTHNSIRFXYCPFUEOCKRNEICTDGYIYZ
# EICTDGYIYZKTHNSIRFXYCPFUEOCKRN

cat /krypton/krypton6/krypton7 
# PNUKLYLWRQKGKBE

echo "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN" > key

KEY=EICTDGYIYZKTHNSIRFXYCPFUEOCKRN
PLAIN=PNUKLYLWRQKGKBE


# host
git clone https://github.com/m-rosinsky/Krypton_Scripts; cp Krypton_Scripts/vignere_decoder.py .; rm -rf Krypton_Scripts
sshpass -p "RANDOM" scp -P 2231 vignere_decoder.py krypton6@krypton.labs.overthewire.org:/tmp/<path>

# krytpon
python3 vignere_decoder.py /krypton/krypton6/krypton7 "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
```

# flag
LFSRISNOTRANDOM