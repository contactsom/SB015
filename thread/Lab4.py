from threading import *

class MyThread:
    def display(self):
        for i in range(1,6):
            print("Child Thread")


t=MyThread() # Object
thread=Thread(target=t.display())
thread.start()
