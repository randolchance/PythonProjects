# PROJECT EULER PROBLEM 387 - Harshad Numbers

import sys
import os
sys.path.insert(0,os.path.expanduser("~/PythonProjects/venvBigFloat/lib/python3.5/site-packages"))
from gmpy import is_prime
#import primeCheckII as PC

def isHarshad(x):
    digit_sum = sum([int(s) for s in str(x)])
    return(x%digit_sum == 0)

def isStrongHarshad(x):
    digit_sum = sum([int(s) for s in str(x)])
    return(x%digit_sum == 0 and is_prime(x//digit_sum))

def isRightTruncHarshad(x):
    while isHarshad(x):
        x = int(str(x)[:-1])
        if len(str(x)) == 1:
            return(True)
    return(False)

"""
total = 0
for p in PC.primes(10,10000):
    n = p//10
    if isStrongHarshad(n) and rightTruncHarshad(n):
        total += p
print(total)
"""

MAX_DIGITS = 14

def makePrimeHarshads(max_digits,digits,aTotal):
    if digits == 0:
        for n in range(1,10):
            yield(str(n))
    else:
        for harshad in makePrimeHarshads(max_digits,digits-1,aTotal):
            for n in range(10):
                new_harshad = int(harshad+str(n))
                if isHarshad(new_harshad):
                    yield(str(new_harshad))
                elif is_prime(new_harshad):
                    if isStrongHarshad(int(harshad)):
                        #print(new_harshad)
                        aTotal[0] += new_harshad
                

total = [0]
for n in makePrimeHarshads(MAX_DIGITS-1,MAX_DIGITS-1,total):
    print(n,total)

print(total)

