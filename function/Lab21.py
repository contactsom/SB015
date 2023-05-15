print("Start : Example for Function ")

def m1():
    a = 10 # Local variable scope is within m1() function
    print(a)

def m2():
    print(a) # Error

def m3():
    print(a) # Error

#calling
m1()
m2()
m3()
print("End : Example for Function  ")