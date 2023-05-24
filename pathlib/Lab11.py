from pathlib import Path
from shutil import copyfile


path=Path('/Users/om/SB015/pathlib/Lab1.py')
home = path.home()
print(home)


relativepath=path.relative_to(home)
print(relativepath)


