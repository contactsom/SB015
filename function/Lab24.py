print("Start : Example for Function ")

a = 10 # Global Variable

def m1():
    a = 1111  # Local Variable
    print(a) # 1111
    print(globals() ['a'])  # 10

def m2():
    print(a) # 10

def m3():
    print(a) # 10

#calling
m1()
m2()
m3()
print("End : Example for Function  ")