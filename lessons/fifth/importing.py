import multiprocessing as mp
from multiprocessing import cpu_count

print(mp.cpu_count())
print(cpu_count())

from csv import reader as csvreader

import os.path

os.path.isdir('./')
