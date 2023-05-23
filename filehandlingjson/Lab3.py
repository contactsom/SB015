import json

teacherdata = {
                "NAME":"Mohan",
                "PHONE":"12345",
                "EMAIL":"mohan@abc.com",
                "DOMAIN":"IT",
                "SUBJECT":["JAVA","PYTHON","C","C++"]
               }

with open("teachers.json","w") as file:
    json.dump(teacherdata,file)


