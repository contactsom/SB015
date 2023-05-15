print("Start : Example for Function ")

''' SOLUTION : 4. Variable Length Arguments '''

def getSumofTwoNumber(*values):
    sum = 0
    for  a  in values:
        sum = sum +a
    return sum


output1=getSumofTwoNumber(1)
print("Sum of One Number : ",output1)
output2=getSumofTwoNumber(1,2)
print("Sum of Two Number : ",output2)
output3=getSumofTwoNumber(1,2,3)
print("Sum of Three Number : ",output3)
output4= getSumofTwoNumber(1,2,3,4)
print("Sum of Four Number : ",output4)
output5=getSumofTwoNumber(1,2,3,4,5)
print("Sum of Five Number : ",output5)
output6=getSumofTwoNumber(1,2,3,4,5,6)
print("Sum of Six Number : ",output6)

print("End : Example for Function  ")