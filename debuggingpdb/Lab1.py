import pdb

def addition(a,b):
    #result = a * b  # ERROR
    result = a+b
    return result

pdb.set_trace() # From where you want to do the debugging


'''
# Error as Input coming in the form of String
x = input("Enter the First Number")
y = input("Enter the Second Number")
'''

x = int(input("Enter the First Number"))
y = int(input("Enter the Second Number"))

sum=addition(x,y)
print(sum)





