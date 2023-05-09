print("START- This is Example for For Loop Over List ")

# -Ve  =   -5,  -4  -3, -2, -1
# List =  [ 10, 20, 30, 40, 50 ]
# +Ve  =    0,  1,   2,  3,  4

print("------------------------------------------------------")

list =   [ 10, 20, 30, 40, 50 , 22, 23,45,78,99]

print("-----------------------EVEN NUMBER-------------------------------")
for  l in list:
    if(l%2==0):
        print(l)


print("-----------------------ODD NUMBER-------------------------------")
for  l in list:
    if(l%2!=0):
        print(l)
print("END- This is Example for While Loop Over List ")