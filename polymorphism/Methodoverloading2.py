class Methodoverloading2:

    def m1(self, a, b):
        print("Method with two Argument...-2")

    def m1(self):
        print("Method with two Argument...-0")

    def m1(self, a):
        print("Method with two Argument...-1")


o1=Methodoverloading2()
#o1.m1() # TypeError: Methodoverloading2.m1() missing 1 required positional argument: 'a'

o1.m1(10)

#o1.m1(10,20)