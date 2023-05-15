print("Start : Example for Function ")

# Write a recursive function code to find the factorials of the number
# Ex : factorial of 5 = 5*4*3*2*1 ,
# Factorial of 0 = 1

def factorial(n):
    if(n==0):
        result = 1
    else:
        result=n*factorial(n-1)
    return result

output=factorial(5)
print(output)

print("End : Example for Function  ")