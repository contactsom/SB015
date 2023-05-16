'''
    How to Create the Custom Exception
'''

class IdCardNotFoundException(Exception):
    def __init__(self,args):
        self.msg=args


#swap ="Success"
swap ="Fail"

if swap=="Fail":
    raise IdCardNotFoundException("Please wait we will working on to get the temporary ID Card")
else:
    print("Welcome to office, Have a nice day")

