# PROJECT EULER PROBLEM 92 - Square Digit Chains

from memoise import Memoise
import sys

sys.setrecursionlimit(2000)

@Memoise
def squareDigitChain(n):
    if n == 1 or n == 89:
        return(n)
    str_n = str(n)
    S = sum([int(s)**2 for s in str_n])
    return(squareDigitChain(S))

max_n = 9999999

total = 0
for n in range(1,max_n+1):
    if n%10000 == 0:
        print(n)
    S = squareDigitChain(n)
    total += (S == 89)

print(total)

