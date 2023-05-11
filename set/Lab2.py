print("START- This is Example for Set  Using Range Function ")

mySet= set(range(5)) # I need five number start from, zero
print(mySet) # {0, 1, 2, 3, 4}
print(type(mySet)) # <class 'set'>

print("---------------------------------")

mySet1= set(range(0,15))
print(mySet1) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
print(type(mySet1)) # <class 'set'>


print("---------------------------------")

mySet2= set(range(0,15,2))
print(mySet2) # {0, 2, 4, 6, 8, 10, 12, 14}
print(type(mySet2)) # <class 'set'>


print("---------------------------------")

mySet3= set(range(0,15,3))
print(mySet3) # {0, 3, 6, 9, 12}
print(type(mySet3)) # <class 'set'>

print("END- This is Example for Set ")