print("START- This is Example for Traversing the Tuple Elements , 1. Using While loop")

#   0,   1,   2,   3,    4,   +ve Index Representation
#   10,  20 , 30 , 40 , 50
#  -5,   -4,  -3,  -2,  -1    -ve Index Representation

print("------------------------------")

mytuple=(10,  20 , 30 , 40 , 50)

i = 0
while i<len(mytuple):
    print(mytuple[i])
    i = i+1
