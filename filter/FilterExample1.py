'''
list = 1,4,5,3,6,7,90,56,44

Requirement : I want to filter this list and get the only Even Number
'''

def isEven(listValue):
    if(listValue%2==0):
        print("I am Even")
    else:
        print("I am Odd")


mylist= [1,4,5,3,6,7,90,56,44]

evenList=list(filter(isEven,mylist)) # I want to do the filter against "isEven" rule on data "mylist"
print(evenList)