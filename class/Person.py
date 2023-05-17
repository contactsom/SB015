class Person:
    def __init__(self,name,id,age,address,emailid,gender):
        self._name = name
        self._id = id
        self._age = age
        self._address = address
        self._emailid = emailid
        self._gender = gender

    def getMyDetails(self):
        print("My Name is :",self._name)
        print("My ID is :", self._id)
        print("My AGE is :", self._age)
        print("My Address ID is :", self._address)
        print("My EMail ID is :", self._emailid)
        print("My Gender is :", self._gender)


person = Person("Shrinidhi",101,22,"Bangalore","shrinidhi@abc.com","F")
person.getMyDetails()
