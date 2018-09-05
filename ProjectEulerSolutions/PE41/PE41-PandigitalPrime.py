# PROJECT EULER PROBLEM 41 - Pandigital Prime

import primeCheckII
from permutations import permutation

BAD_END_NUMS = [2,4,5,6,8]

def findPanPrime():
    for d in range(8,1,-1):
        digits = [x for x in range(1,d)]
        digits.reverse()
        if sum(digits)%3 == 0:
            continue
        for p in permutation(digits,len(digits)):
            if p[-1] not in BAD_END_NUMS:
                n = int("".join([str(x) for x in p]))
                if primeCheckII.PrimeCheck(n):
                    return(n)

print(findPanPrime())

