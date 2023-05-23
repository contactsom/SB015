print("START : This is the Example of Text File Handling ")

file=open("simple.txt",'w')

print("File Name :", file.name)
print("File Mode :", file.mode)

print("Is this File in Redable Mode  :", file.readable())
print("Is this File in Writable Mode  :", file.writable())

print("Is this File Closed : ",file.closed)
file.close()
print("Is this File Closed : ",file.closed)

print("END : This is the Example of Text File Handling ")