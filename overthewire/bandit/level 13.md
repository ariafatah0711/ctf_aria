# soal
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. \
For this level it may be useful to create a directory under /tmp in which you can work. \
Use mkdir with a hard to guess directory name. Or better, use the command “mktemp -d”. Then copy the datafile using cp, and rename it using mv (read the manpages!)

# solve
```bash
# change the workdir to value (command mktemp -d)
# mktemp -d use for create random tmp
WORKDIR=$(mktemp -d)
cd $WORKDIR
cp /home/bandit12/data.txt .

# hexdump
xxd -r data.txt data

# 1
file data
# data: gzip compressed data, was "data2.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 574
mv data data.gz
gunzip data.gz # OR tar xfz data.gz

# 2
file data
# data: bzip2 compressed data, block size = 900k
bunzip2 data

# 3
file data.out 
# data.out: gzip compressed data, was "data4.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 20480
mv data.out data.gz
gunzip data.gz

# 4
file data
# data: POSIX tar archive (GNU)
tar xf data

# 5
file data5.bin 
# data5.bin: POSIX tar archive (GNU)
tar xf data5.bin

# 6
file data6.bin 
# data6.bin: bzip2 compressed data, block size = 900k
bunzip2 data6.bin

# 7
file data6.bin.out 
# data6.bin.out: POSIX tar archive (GNU)
tar xf data6.bin.out

# 8
file data8.bin 
# data8.bin: gzip compressed data, was "data9.bin", last modified: Thu Sep 19 07:08:15 2024, max compression, from Unix, original size modulo 2^32 49
mv data8.bin data8.gz
gunzip data8.gz

# read
cat data8
# The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

# flag
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn