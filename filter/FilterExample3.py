'''
list = 1,4,5,3,6,7,90,56,44

Requirement : I want to filter this list and get the only Even Number
'''

def isEven(listValue):
    oddlist=[]

    if(listValue%2!=0):
        oddlist.append(listValue)
    return oddlist

mylist= [1,4,5,3,6,7,90,56,44]

oddList=list(filter(isEven,mylist)) # I want to do the filter against "isEven" rule on data "mylist"
print(oddList)