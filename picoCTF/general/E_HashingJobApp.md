# soal
If you want to hash with the best, beat this test! \
Additional details will be available after launching your challenge instance.

## launch istance
If you want to hash with the best, beat this test! \
nc saturn.picoctf.net 60686

# hint
- You can use a commandline tool or web app to hash text
- Press Ctrl and c on your keyboard to close your connection and return to the command prompt.

# solve
```bash
nc saturn.picoctf.net 60686
# Please md5 hash the text between quotes, excluding the quotes: 'alien abductions'
# Answer: 
0d46a3ff4160862bb8329524b99da972
# 0d46a3ff4160862bb8329524b99da972
# Correct.
# Please md5 hash the text between quotes, excluding the quotes: 'armed robbery'
# Answer:
986ad0db60b8d3d46281880f693a5926
# 986ad0db60b8d3d46281880f693a5926
# Correct.
# Please md5 hash the text between quotes, excluding the quotes: 'having a baby'
# Answer:
e215dac50d263755ea60abc80a0f3437
# e215dac50d263755ea60abc80a0f3437
# Correct.
# picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}

## u can use tool online encode to md5
##  python3

print(hashlib.md5(b"having a baby").hexdigest())
# e215dac50d263755ea60abc80a0f3437
```

# flag
picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}