
mylist = [1,2,3,4,5,6,7,8]
# Requirement is : I want to double each element of list

def doubleList(mylist):
    return mylist*2

doublelist=list(map(doubleList,mylist))
print(doublelist)
