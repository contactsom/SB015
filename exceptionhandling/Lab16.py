import os

try:
   a = int(input("Enter the First Number :: "))
   b = int(input("Enter the Second Number :: "))
   print(a/b)

except ZeroDivisionError as msg:
   print("This is the Exception :: ", msg)
   print("This is Default response form ZeroDivisionError  ")
   os._exit(0) # Tremonation of Python Compiler on python 2

except ValueError as msg:
    print("This is the Exception :: ",msg)
    print("This is Default response form ValueError  ")
    os._exit(0) # Tremonation of Python Compiler on python 2

finally:
    print("FINALY:: I will execute always no matter if try block have error or not ")

print("Statement -5 ")