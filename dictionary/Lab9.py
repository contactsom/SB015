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


if 3135 in empIdEmployee:
    del empIdEmployee[3135]
else:
    print("Can not Delete as Key Not Exist")

print(empIdEmployee)

print("-------------After Delete --------------------")
#del empIdEmployee[2222] # KeyError: 2222

if 2222 in empIdEmployee:
    del empIdEmployee[2222]
else:
    print("Can not Delete as", 2222, "Not Exist")

print(empIdEmployee)

print("END- This is Example for Dictionary ")