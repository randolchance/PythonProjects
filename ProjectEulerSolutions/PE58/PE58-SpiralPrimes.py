# PROJECT EULER PROBLEM 58 - Spiral Primes

"""
The next four corner numbers obey the rules:
TR: previousBR + size-1
TL: TR + size-1
BL: TL + size-1
BR: BL + size-1
then increase size by 2
"""

from math import sqrt

import primeCheckII


size = 1
ratio = 1.0
check_list = []
TR = TL = BL = BR = 1
prime_count = 0
while ratio >= 0.1:
    size += 2
    TR = BR + size-1
    TL = TR + size-1
    BL = TL + size-1
    BR = BL + size-1
    check_list = [TR,TL,BL,BR]
    total = 2*(size-1) + 1
    for x in check_list:
        if primeCheckII.PrimeCheck(x):
            prime_count += 1
    ratio = prime_count / total
    print(ratio)
print(prime_count,total,ratio,size)








