print("START- This is Example for Dictionary ")

# K - Employee ID - int
# V - Employee Name - String

empIdEmployee= {
                3132:"Rajnish",
                3133:"awadhesh",
                3134:"Ashutosh",
                3135:"John",
                8000:"ABC"
                }
print("---------------------------------")

print(empIdEmployee)

#print(empIdEmployee[8000]) # KeyError: 8000

empIdEmployee.setdefault(8000,"DEFAULT NAME")

print(empIdEmployee[8000]) #ABC

'''
If KEY Exist it will give you the respective Value
    Where as , If KEY not Exist it will give you the setdefault() Value
'''

print("END- This is Example for Dictionary ")