print("START : This is the Example of Text File Handling ")

with open("employee.txt",'r') as file:
    print(file.read())
    print("Is my File Got Closed :: ", file.closed) # false

print("Is my File Got Closed :: ",file.closed) # True




print("END : This is the Example of Text File Handling ")