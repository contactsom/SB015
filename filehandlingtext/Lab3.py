print("START : This is the Example of Text File Handling ")

#file=open("abc.txt",'w') # First Argument is file Name , File Mode
file=open("abc.txt",'a')

file.write("******************************\n")
file.write("I am Line No 1 \n")
file.write("I am Line No 2 \n")
file.write("I am Line No 3 \n")
file.write("I am Line No 4 \n")
file.write("I am Line No 5 \n")

file.write("******************************\n")

file.write("I am NEW  Line No 11 \n")
file.write("I am NEW  Line No 21 \n")
file.write("I am NEW  Line No 31 \n")
file.write("I am NEW  Line No 41 \n")
file.write("I am NEW  Line No 51 \n")
file.write("******************************\n")

file.close()


print("END : This is the Example of Text File Handling ")