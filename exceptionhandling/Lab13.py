
try:
   a = int(input("Enter the First Number :: "))
   b = int(input("Enter the Second Number :: "))
   print(a/b)

except ZeroDivisionError as msg:
   print("This is the Exception :: ", msg)
   print("This is Default response form ZeroDivisionError  ")

except ValueError as msg:
    print("This is the Exception :: ",msg)
    print("This is Default response form ValueError  ")

print("Statement -5 ")