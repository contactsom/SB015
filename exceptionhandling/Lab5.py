print("Hello Welcome to Simplilearn Python Class")

def devideNumber(a,b):
    c = 0
    try:
        c = a/b
    except:
        print("Envalid Number Entred")
    return c


output1=devideNumber(10,2)
print(output1)

output2=devideNumber(10,5)
print(output2)

output3=devideNumber(10,0) # ZeroDivisionError: division by zero
print(output3)

output4=devideNumber(20,5)
print(output4)