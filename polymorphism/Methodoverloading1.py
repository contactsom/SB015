class Methodoverloading1:

    def m1(self):
        print("Method with two Argument...-0")

    def m1(self, a):
        print("Method with two Argument...-1")

    def m1(self, a, b):
        print("Method with two Argument...-2")


o1=Methodoverloading1()
#o1.m1() # TypeError: Methodoverloading1.m1() missing 2 required positional arguments: 'a' and 'b'

#o1.m1(10) # TypeError: Methodoverloading1.m1() missing 1 required positional argument: 'b'

o1.m1(10,20)