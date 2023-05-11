print("START- This is Example for Accessing Elements of Tuple - By Using Index")

#   0,   1,   2,   3,    4,   +ve Index Representation
#   10,  20 , 30 , 40 , 50
#  -5,   -4,  -3,  -2,  -1    -ve Index Representation

print("------------------------------")

mytuple=(10,  20 , 30 , 40 , 50)

print("[2:5]",mytuple[2:5]) # 30 , 40 , 50
print("[2:5000]",mytuple[2:5000]) # 30 , 40 , 50
print("[2:]",mytuple[2:]) # 30 , 40 , 50
print("[:4]",mytuple[:4]) # 30 , 40 , 50


print("------------------------------")


print("[-2:5]",mytuple[-2:5])
print("[-2:-5]",mytuple[-2:-5])
print("[-5:-2]",mytuple[-5:-2])





print("END- This is Example for Tuple ")