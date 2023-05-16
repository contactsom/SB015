
try:
    print("I am Try")

except ZeroDivisionError:
    print("I am Except")

else :
    print("I am Else")
    print("ELSE block will get executed when try block does not have any error")

finally:
    print("I am Finally")

