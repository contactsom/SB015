class University:
    def __init__(self,name,id,age,address,emailid):
        self._name = name
        self._id = id
        self._age = age
        self._address = address
        self._emailid = emailid


    def getMyDetails(self):
        print("My University Name is :",self._name)
        print("My University ID is :", self._id)
        print("My University AGE is :", self._age)
        print("My University Address ID is :", self._address)
        print("My University EMail ID is :", self._emailid)



university = University("TMBU",1001,99,"Bihar","tmbu@abc.com")
university.getMyDetails()

print("*******************************************************************")

print("My University Name is :", university._name)
print("My University ID is :", university._id)
print("My University AGE is :", university._age)
print("My University Address ID is :", university._address)
print("My University EMail ID is :", university._emailid)