import subprocess

def executeC():
    s=subprocess.check_call("gcc HelloWorld.c -o out1;./out1",shell=True)
    print(", return code",s)

def executeCPP():
    s=subprocess.check_call("g++ HelloWorld.cpp -o out2;./out2",shell=True)
    print(", return code",s)

def executeJAVA():
    s=subprocess.check_call("javac HelloWorld.java; java HelloWorld",shell=True)
    print(", return code",s)


if __name__== "__main__":
    executeC()
    executeCPP()
    executeJAVA()
