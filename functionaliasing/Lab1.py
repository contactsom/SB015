def wish(name):
    print("Good Morning", name)

greeting=wish # Creating the Alias of the function "wish" name "greeting"

print(id(wish)) # 4380016448
print(id(greeting)) # 4380016448

wish("Mohan")