# soal
People keep trying to trick my players with imitation flags. \
I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. \
Additional details will be available after launching your challenge instance.

## launch istance
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. \
ssh -p 64500 ctf-player@rhea.picoctf.net \
Using the password 1db87a14. Accept the fingerprint with yes, and ls once connected to begin. \

Remember, in a shell, passwords are hidden! \
Checksum: 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a \
To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.

# hint
- Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.
- You can create a SHA checksum of a file with sha256sum <file> or all files in a directory with sha256sum <directory>/*.
- Remember you can pipe the output of one command to another with |. Try practicing with the 'First Grep' challenge if you're stuck!

# solve
```bash
ssh -p 64500 ctf-player@rhea.picoctf.net
# pass: 1db87a14

ls
checksum.txt  decrypt.sh  files

./decrypt.sh
# Expected usage: decrypt.sh <filename>

./decrypt.sh checksum.txt
# bad magic number
# Error: Failed to decrypt 'checksum.txt'. This flag is fake! Keep looking!

sha256sum files/* | grep -i "55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a"
# 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de

./decrypt.sh files/2cdcb2de
# picoCTF{trust_but_verify_2cdcb2de}
```

# flag
picoCTF{trust_but_verify_2cdcb2de}