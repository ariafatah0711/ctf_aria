# soal
Reception of Special has been cool to say the least. \
That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. \
With Specialer, we really tried to remove the distractions from using a shell. \
Yes, we took out spell checker because of everybody's complaining. \
But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. \
Please start an instance to test your very own copy of Specialer. \
Additional details will be available after launching your challenge instance.

## launch istance
ssh -p 64911 ctf-player@saturn.picoctf.net. \
The password is fd7746b4

# hint
- What programs do you have access to?

# solve
```bash
ssh -p 64911 ctf-player@saturn.picoctf.net
# pass: fd7746b4

## jika di tab ternyata terdapat beberapa command hanya saja tidak semuanya bisa

echo $(< ala/kazam.txt)
# return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}
```

# flag
```bash
picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}
```