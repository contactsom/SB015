from zipfile import *

zipfile=ZipFile("simplilearn.zip",'w',ZIP_DEFLATED)
zipfile.write("bookauthor.csv")
zipfile.write("employee.txt")
zipfile.write("NEW_simplilearn-logo.png")
zipfile.write("teacher.json")
zipfile.close()


