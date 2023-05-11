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
print("-------------Before Update --------------------")

print(empIdEmployee[3132]) # Rajnish

print("-------------After Update --------------------")

empIdEmployee[3132] = "RAJA"

print(empIdEmployee[3132]) # RAJA
print("END- This is Example for Dictionary ")