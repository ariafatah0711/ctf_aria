# soal
https://ringzer0ctf.com/files/329d7767b42f3d8e9f498e98fbabc83c.zip \
MD5 sum: 329d7767b42f3d8e9f498e98fbabc83c

# solve
```bash
wget --header="Cookie: PHPSESSID=<value>" https://ringzer0ctf.com/files/329d7767b42f3d8e9f498e98fbabc83c.zip
md5sum 329d7767b42f3d8e9f498e98fbabc83c.zip | grep 329d7767b42f3d8e9f498e98fbabc83c
# 329d7767b42f3d8e9f498e98fbabc83c  329d7767b42f3d8e9f498e98fbabc83c.zip

unzip 329d7767b42f3d8e9f498e98fbabc83c.zip
cd Policies
grep -r ./

exiftool {75DE8F0A-DEC0-441F-AE29-90DFAFCF632B}/User/Preferences/Groups/Groups.xml | grep Group
# Groups User Properties Cpassword: PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw

docker run grimhacker/gp3finder --help
docker run grimhacker/gp3finder -D PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw
# INFO: gp3finder: Decrypted password is 10 characters.
# INFO: gp3finder: ----------
# INFO: gp3finder: LocalRoot!
# INFO: gp3finder: ----------
```

- https://grimhacker.com/2015/04/10/gp3finder-group-policy-preference-password-finder
- https://jdsecdef.github.io/Finding-and-Decrypting-cpasswords-in-Group-Policy-Preferences/
- https://faresbltagy.gitbook.io/footprintinglabs/soc-hackthebox-notes-and-labs/windows-attacks-and-defense/gpp-passwords

# flag
LocalRoot!