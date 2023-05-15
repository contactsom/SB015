print("Start : Example for Function ")

a = 10

def m1():
    a = 1111 # Although Variable name is same , Here it says you have the local variable why you go for global
    print(a) # 1111

def m2():
    print(a) # 10 You do not have local variable get from the global variable

def m3():
    print(a) # 10 You do not have local variable get from the global variable

#calling
m1()
m2()
m3()
print("End : Example for Function  ")