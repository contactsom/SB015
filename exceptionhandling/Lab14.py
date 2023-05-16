
try:
   a = int(input("Enter the First Number :: "))
   b = int(input("Enter the Second Number :: "))
   print(a/b)

except ZeroDivisionError as msg:
   print("This is the Exception :: ", msg)
   print("This is Default response form ZeroDivisionError  ")

finally:
    print("FINALY:: I will execute always no matter if try block have error or not ")