print("START- This is Example for len() function in  List ")


#         (0-5),(1-5),(2-5),(3-5),(4-5) = (i - x ) , Where i is +Ve index and x is length of list
# -Ve  =   -5,   -4   -3,    -2,    -1
# List =  [ 10,  20,  30,    40,    50 ]
# +Ve  =    0,    1,    2,     3,    4

list =  [ 10, 20, 30, 40, 50 ]
lengthofList=len(list)


print("------------------------------------------------------")

for i in range(lengthofList):
    print(list[i]," Is available at positeve index :",i," And at the negative index : ", i-lengthofList)


print("END- This is Example for While Loop Over List ")