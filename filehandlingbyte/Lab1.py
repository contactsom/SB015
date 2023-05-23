inputfile=open("simplilearn-logo.png",'rb')

outputfile=open("NEW_simplilearn-logo.png",'wb')

inputbyte=inputfile.read()

outputfile.write(inputbyte)

