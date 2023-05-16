
def decor(func):
    def inner(name):
        if(name=="Sahan"):
            print("Hello Sahan Very Good Morning !!!")
        else:
            func(name)
    return inner



@decor
def wish(name):
    print("Hello ",name," Good Morning")


wish("Sunny") # Hello Sunny Good Morning
wish("Sahan") # Requirement : Hello Sahan Very Good Morning !!!
wish("Nithyanandham") # Hello Nithyanandham Good Morning
