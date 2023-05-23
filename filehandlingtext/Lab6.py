print("START : This is the Example of Text File Handling ")


file=open("book.txt",'r')

date=file.read(10) # 10 Character From the File
print(date)

file.close()



print("END : This is the Example of Text File Handling ")