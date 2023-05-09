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

print("-----------------------------------")
print("**** +Ve Index Representation ****")
print("-----------------------------------")
mystring="ABCDEFGH"
print(mystring)                #ABCDEFGH
print("[1:5]",mystring[1:5])   #BCDE
print("[0:0]",mystring[0:0])   #
print("[0:8]",mystring[0:8])   #ABCDEFGH
print("[0:80]",mystring[0:80]) #ABCDEFGH
print("[0:9]",mystring[0:9])   #ABCDEFGH
print("[:9]",mystring[:9])     #ABCDEFGH
print("[0:]",mystring[0:])     #ABCDEFGH
print("[:]",mystring[:])       #ABCDEFGH


print("END- This is Example for String Slicing in ")

