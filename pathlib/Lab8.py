from pathlib import Path
from shutil import copyfile

# /Users/om/SB015/pathlib/Lab1.py

path=Path('/Users/om/SB015/pathlib/Lab1.py')
print(path)

print(path.as_uri())
print(path.as_posix())

