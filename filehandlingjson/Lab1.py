import json


teacherdata = {
                "NAME":"Mohan",
                "PHONE":"12345",
                "EMAIL":"mohan@abc.com",
                "DOMAIN":"IT"
               }

with open("teacher.json","w") as file:
    json.dump(teacherdata,file)
