print("START- This is Example for Dictionary ")

# K - Employee ID - int
# V - Employee Name - String

empIdEmployee= {
                3132:"Rajnish",
                3133:"awadhesh",
                3134:"Ashutosh",
                3135:"John"
                }

print(empIdEmployee)
print("---------------------------------")

if 1111 in empIdEmployee:
    print(empIdEmployee[1111]) #


print("---------------------------------")

if 3134 in empIdEmployee:
    print(empIdEmployee[3134]) #Ashutosh


print("---------------------------------")

if 1111 in empIdEmployee:
    print(empIdEmployee[1111])
else:
    print("KEY not Exist")


print("---------------------------------")

if 3135 not in empIdEmployee:
    print(empIdEmployee[3135])
else:
    print("Not in KEY not Exist")


print("---------------------------------")


print("END- This is Example for Dictionary ")