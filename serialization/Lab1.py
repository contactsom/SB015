import pickle


teacherdata= {
                "NAME" : "MOHAN",
                "EMAIL" : "mohan@simplilearn.com",
                "DOMAIN" : "IT",
                "PASSWORD" : "kcbikbowdnco"
            }

#serialization
with open("teacher.pickle",'wb') as writefile:
    pickle.dump(teacherdata,writefile)

print("Writing the Object in to file teacher.pickle",teacherdata)


#deserialization
with open("teacher.pickle",'rb') as reafile:
    teacherdata_byte=pickle.load(reafile)

print("Reading the Object in to file teacher.pickle",teacherdata_byte)

if teacherdata==teacherdata_byte:
    print("serialization and deserialization Done Successfully")
else:
    print("serialization and deserialization NOT Done Successfully")