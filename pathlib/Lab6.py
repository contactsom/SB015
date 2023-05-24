from pathlib import Path
from shutil import copyfile

homepath= Path().home()

print(homepath) # /Users/om

newPath=homepath / 'SB015'
print(newPath)

newPath1=newPath / 'pathlib'
print(newPath1)

# /Users/om/SB015/pathlib/Lab6.py

