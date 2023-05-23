import json


with open("teachers.json","r") as file:
    data=json.load(file)
    print(data)

#'SUBJECT': ['JAVA', 'PYTHON', 'C', 'C++']}
    print(data['SUBJECT'][0])
    print(data['SUBJECT'][1])
    print(data['SUBJECT'][2])
    print(data['SUBJECT'][3])

