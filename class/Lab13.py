'''
- Return the referance count of the object
- The count returned is generally one higher than you might expect
- Why- Because it include the (temporary ) reference as an argument for getrefcount()

'''
import sys


class Lab13:
    def data(self):
        print("I am from data Function")

lab1=Lab13()
test1=lab1
test2=lab1
test3=lab1
test4=lab1


print(sys.getrefcount(lab1))







