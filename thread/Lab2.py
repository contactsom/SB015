from threading import *

def currentThead():
    for i in range(1,5):
        print("**** Hello I am Child Thread ****")


t=Thread(target=currentThead()) # Thread Creation
t.start() # Starting the thread

for i in range(1, 5):
    print("**** Hello I am Main Thread ****")