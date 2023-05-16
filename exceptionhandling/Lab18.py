
try:
    print("I am Try")
    print(10/0)

except ZeroDivisionError:
    print("I am Except")

else :
    print("I am Else")
    print("ELSE block will Not get executed when try block have any error")

finally:
    print("I am Finally")

