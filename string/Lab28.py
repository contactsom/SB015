
def operatingSystem(name):
    print("Welcome to Operating System :", name)


windows = operatingSystem
print("ID of Function Name operatingSystem ", id(operatingSystem))
print("ID of Function Name windows ", id(windows))

operatingSystem('windows ')
windows('windows')
