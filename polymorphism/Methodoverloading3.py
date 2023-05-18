class Methodoverloading3:
    def getSum(self, a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("Sum of Three Number ",a,b,c ," is : ", a+b+c)
        elif(a!=None and b!=None):
            print("Sum of Two Number ", a, b ," is : ", a + b )
        elif (a != None):
            print("Sum of One Number ", a," is : ", a )
        else:
            print("Please provide at least one argument  " )



o1=Methodoverloading3()

o1.getSum(1,2,3) # 6
o1.getSum(1,2) # 3
o1.getSum(1) # 1
o1.getSum()