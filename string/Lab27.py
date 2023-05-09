print("START- This is Example for String Slicing in")

# INDEX REPRESENTATION

#  0  1  2  3  4  5   6  7 :: +Ve Index Representation
#  A  B  C  D  E  F   G  H
# -8 -7 -6 -5 -4 -3  -2 -1 :: -Ve Index Representation

# [ m:n]
# Where m - Start Point or FROM
# Where n - End Point or TO
# [FROM : TO ]
# where n = (TO-1)
# and m < n

print("-----------------------------------")
print("**** -Ve Index Representation ****")
print("-----------------------------------")
mystring="ABCDEFGH"
print(mystring)

print("[-0,-0]",mystring[-0:-0]) # No Output
print("[-1,-0]",mystring[-1:-0]) # No Output
print("[-1,-1]",mystring[-1:-1]) # No Output
print("[-1,-4]",mystring[-1:-4]) # No Output

print("[-8:-2]",mystring[-8:-2]) # ABCDEF
print("[-8:-2]",mystring[-6:-1]) # CDEFG


print("END- This is Example for String Slicing in ")

