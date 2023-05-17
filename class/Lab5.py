class Student:
    def __init__(self):
        self.name=""
        self.age=None
        self.salary=6000

    def getDetails(self):
        print("Hello I am ",self.name)
        print("Hello My Age is ", self.age)
        print("Hello My Salary is ", self.salary)

student=Student() # Creating the Object of Student Class. Here Object name is "student"

student.getDetails()