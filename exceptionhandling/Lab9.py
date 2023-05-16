
try:
    print("Statement -1 ")
    print(10/0)
    print("Statement -2 ")
except ZeroDivisionError:
    print("Statement -3 ")
    print(10 / 2)
    print("This is Default response In case Error in Try Block  ")
print("Statement -5 ")