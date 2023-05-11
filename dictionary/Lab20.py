print("START- This is Example for Dictionary ")

# K - Employee ID - int
# V - Employee Name - String

empIdEmployee= {
                3132:"Rajnish",
                3133:"awadhesh",
                3134:"Ashutosh",
                3135:"John"
                }
print("---------------------------------")

print(empIdEmployee)

#print(empIdEmployee[8000]) # KeyError: 8000

empIdEmployee.setdefault(8000,"DEFAULT NAME")

print(empIdEmployee[8000]) #ABC


empIdEmployee.setdefault(8000,"DEFAULT NAME LATEST")


'''
If KEY Exist it will give you the respective Value
    Where as , If KEY not Exist it will give you the setdefault() Value
'''

'''
    If you try to do setdefault() more than once :
        Then the Oldest/First value only comes under the Consideration 

'''
print("END- This is Example for Dictionary ")