'''
mylist= [1,4,5,3,6,7,90,56,44]

Requirement : I want to filter this list and get the only Even
'''

mylist= [1,4,5,3,6,7,90,56,44]

evenlist=list( filter(lambda listValue:listValue%2==0,mylist))
print(evenlist)
