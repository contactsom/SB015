print("Start : Example for Function ")

a = 10

def m1():
    global a # Making your local variable to global
    a = 1111
    print(a) #

def m2():
    print(a) #

def m3():
    print(a) #

#calling
m1()
m2()
m3()
print("End : Example for Function  ")