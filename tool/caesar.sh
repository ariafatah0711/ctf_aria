# Caesar cipher encoding
echo "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" | tr '[A-Z]' '[X-ZA-W]'
# output: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

# Caesar cipher decoding
echo "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD" | tr '[X-ZA-W]' '[A-Z]'
# output: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG


# Can also be adjusted to ROT13 instead
echo "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" | tr '[A-Z]' '[N-ZA-M]'
# output: GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT

echo "GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT" | tr '[N-ZA-M]' '[A-Z]'
# output: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG


# Case-sensitive version of ROT13
tr '[A-Za-z]' '[N-ZA-Mn-za-m]'