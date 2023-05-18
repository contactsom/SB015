class Constructoroverloading1:
    def __init__(self):
        print("No Argument Constructor")

    def __init__(self,a):
        print("One Argument Constructor")

    def __init__(self,a,b):
        print("Two Argument Constructor")



o1=Constructoroverloading1() # TypeError: Constructoroverloading1.__init__() missing 2