import getpass

try:
    p=getpass.getpass()
except Exception as error:
    print("Exception ", error)
else:
    print("Passwored Entred",p)