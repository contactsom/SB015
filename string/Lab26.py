print("START- This is Example for String Slicing in")

# INDEX REPRESENTATION

#  0  1  2  3  4  5   6  7 :: +Ve Index Representation
#  A  B  C  D  E  F   G  H
# -8 -7 -6 -5 -4 -3  -2 -1 :: -Ve Index Representation

# [ m:n:i]
# Where m - Start Point or FROM
# Where n - End Point or TO
# i       - Interval
# [FROM:TO:INTERVAL]


print("-----------------------------------")
print("**** +Ve Index Representation ****")
print("-----------------------------------")
mystring="ABCDEFGH"
print(mystring)                        #ABCDEFGH
print("[0:5:1]",mystring[0:5:1])       # ABCDE
#print("[0:5:1]",mystring[0:5:0])       # ValueError: slice step cannot be zero
print("[0:5:2]",mystring[0:5:2])       # ACE
print("[0:5:2]",mystring[0:7:3])       # ADG
print("[0:5:2]",mystring[0:7:2])       # [A]  B  [C]  D  [E]  F   [G]



print("END- This is Example for String Slicing in ")

