class Methodoverloading4:
    def getSum(self, *a):
        sum = 0
        for x in a:
            sum = sum+x
        print("SUM :",sum)


o1=Methodoverloading4()
o1.getSum()
o1.getSum(1)
o1.getSum(1,2)
o1.getSum(1,2,3)
o1.getSum(1,2,3,4,5,6,7,8,9,10)


