'''
1. Operator Overloading on object
    + Operator Overloading
'''

class Operatoroverloading3:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        print(self.name)
        print(other.name)
        return self.name + other.name

o1=Operatoroverloading3(" Sahan ")
o2=Operatoroverloading3(" Gowda ")

print(o1+o2) # Sahan  Gowda