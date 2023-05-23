print("START : This is the Example of Text File Handling ")

file=open("data.txt",'r')

lines=file.readlines()

for line in lines:
    print(line,end='')


file.close()



print("END : This is the Example of Text File Handling ")