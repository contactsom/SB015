import getpass


sequarityQuestion=getpass.getpass(prompt="What is your Fav Book Name ? ")

if sequarityQuestion.upper()=="PYTHON":
    print("Login Successfullly")
else:
    print("Login Denied")
