# PROJECT EULER PROBLEM 72 - Counting Fractions

from findDivisorsII import findDivisors
from findFactorsII import findFactors
from memoise import Memoise
import primeCheckII

@Memoise
def countFractions(N):
    s = N-1
    if not primeCheckII.PrimeCheck(N):    
        D = findDivisors(N,False,False)
        s -= sum([countFractions(d) for d in D])
    return(s)


max_N = 1000000
total = 0
for N in range(max_N,1,-1):
    if N%1000 == 0:
        print(N)
    total += countFractions(N)

print(total)

