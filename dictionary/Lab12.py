print("START- This is Example for Dictionary ")

# K - Employee ID - int
# V - Employee Name - String

empIdEmployee= {
                3132:"Rajnish",
                3133:"awadhesh",
                3134:"Ashutosh",
                3135:"John"
                }
print("-------------Before Delete --------------------")
print(empIdEmployee)

print("-------------After Delete --------------------")
del empIdEmployee

print(empIdEmployee) # NameError: name 'empIdEmployee' is not defined


print("END- This is Example for Dictionary ")