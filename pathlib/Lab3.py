from pathlib import Path
from os import chdir

p= Path('..')
print("Current Directory ::", Path.cwd())
chdir(p)
print("Current Directory ::", Path.cwd())
chdir(p)
print("Current Directory ::", Path.cwd())