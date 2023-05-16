class Student:
    def setName(self,name):
        self.name=name


    def getName(self):
            return self.name

student=Student()
student.setName("Sahan")

print(student.getName())