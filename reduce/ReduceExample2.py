from functools import reduce

mylist = [1,2,3,4,5,6,7]

result1=reduce(lambda a,b : a*b,mylist) # 28
print(result1)