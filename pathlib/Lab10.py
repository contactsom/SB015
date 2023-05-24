from pathlib import Path
from shutil import copyfile


path=Path('/Users/om/SB015/')

dirs= [e for e in  path.iterdir()  if e.is_dir()]
print(dirs)




