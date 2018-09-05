# PROJECT EULER PROBLEM 80 - Square Root Digital Expansion


import sys
import os
sys.path.insert(0,os.path.expanduser("~/PythonProjects/venvBigFloat/lib/python3.5/site-packages"))
from bigfloat import *
from gmpy import is_square

from memoise import Memoise
import primeCheckII as pc


total = 0
for n in range(1,101):
    if is_square(n): continue
    with precision(1024):
        s = "".join(str(sqrt(n)).split("."))
    S = 0
    for i in range(100):
        S += int(s[i])
    total += S

print(total)

