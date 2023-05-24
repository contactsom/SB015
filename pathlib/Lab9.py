from pathlib import Path
from shutil import copyfile

# /Users/om/SB015/pathlib/Lab1.py

path=Path('/Users/om/SB015/pathlib/Lab1.py')

print("The Part is : ", path.parts)
print("The Drive is : ", path.drive)
print("The Root is : ", path.root)
print("---------------------------")

print("The Name is : ", path.name)
print("The Steam is : ", path.stem)
print("The Anchor is : ", path.anchor)




