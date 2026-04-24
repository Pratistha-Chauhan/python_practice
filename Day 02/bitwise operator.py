#Bitwise operators are used to compare (binary) numbers:
# & (AND) :	Sets each bit to 1 if both bits are 1	[x & y]	
print("& (AND) :",6 & 3)
# |	(OR)  :	Sets each bit to 1 if one of two bits is 1	[x | y]	
print("| (OR)  :",6 & 3)

# ^	(XOR) :	Sets each bit to 1 if only one of two bits is 1	[x ^ y]	
print("^ (XOR) :",6 & 3)

# ~	(NOT) :	Inverts all the bits [~x]
print("~ (NOT) :",6 & 3)

# << (Zero fill left shift)  : Shift left by pushing zeros in from the right and let the leftmost bits fall off	[x << 2]	
print("<< (Zero fill left shift)  :",6 & 3)

# >> (Signed right shift) :	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	[x >> 2]
print(">> (Signed right shift) :",6 & 3)

