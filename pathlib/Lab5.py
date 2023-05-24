from pathlib import Path
from shutil import copyfile

source= Path('employee.txt')
destination= Path('New_employee.txt')

copyfile(source,destination)

