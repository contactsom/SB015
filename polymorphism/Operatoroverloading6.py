'''
2. Operator Overloading
    * Operator Overloading
'''

class Operatoroverloading5:
    def __init__(self,value):
        self.value=value

    def __mul__(self, other):
        return self.value * other.value

o1=Operatoroverloading5(5)
o2=Operatoroverloading5(10)
print(o1*o2) # 50