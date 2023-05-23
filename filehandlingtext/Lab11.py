print("START : This is the Example of Text File Handling ")

file=open("data.txt",'r')
print(file.read())

print("**********************")
file.seek(0)
print(file.read())

file.close()

print("END : This is the Example of Text File Handling ")