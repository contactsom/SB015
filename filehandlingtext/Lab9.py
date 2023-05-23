print("START : This is the Example of Text File Handling ")

with open("employee.txt",'w') as file:
    file.write(" A \n")
    file.write(" B \n")
    file.write(" C \n")
    file.write(" D \n")
    file.write(" E \n")
    print("Is my File Got Closed :: ", file.closed) # false

print("Is my File Got Closed :: ",file.closed) # True




print("END : This is the Example of Text File Handling ")