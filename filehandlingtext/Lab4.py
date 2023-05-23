print("START : This is the Example of Text File Handling ")


file=open("mylist.txt",'a')

list = ["A \n","B \n","C \n","D \n","E \n","F \n","G \n","H \n"]

file.writelines(list)


file.close()


print("END : This is the Example of Text File Handling ")