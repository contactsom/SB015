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

print(empIdEmployee[8000]) #


print("END- This is Example for Dictionary ")