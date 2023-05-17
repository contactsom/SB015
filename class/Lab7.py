class Lab7:
    def __init__(self):
        self.a=10
        self.b = 10
        self.c = 20
        self.d = 30
        self.e = 40
        self.f = 50
        self.g = 60
        self.h = 70
        self.i = 80
        self.j = 90


    def getDetails(self):
        print("Value of a ",self.a)
        print("Value of b ", self.b)
        print("Value of c ", self.c)
        print("Value of d ", self.d)
        print("Value of e ", self.e)
        print("Value of f ", self.f)
        print("Value of g ", self.g)
        print("Value of h ", self.h)
        print("Value of i ", self.i)
        print("Value of j ", self.j)



lab7=Lab7()
lab7.getDetails()
print(lab7.__dict__)
