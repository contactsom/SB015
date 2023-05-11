print("START- This is Example for Dictionary ")

# K - Employee ID - int
# V - Employee Name - String

empIdEmployee= {
                3132:"Rajnish",
                3133:"awadhesh",
                3134:"Ashutosh",
                3135:"John"
                }
print("-------------Before popitem()--------------------")
print(empIdEmployee) # {3132: 'Rajnish', 3133: 'awadhesh', 3134: 'Ashutosh', 3135: 'John'}

print("-------------After popitem()--------------------")
items=empIdEmployee.popitem()
print(items) # (3135, 'John')


print("END- This is Example for Dictionary ")