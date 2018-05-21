from math import sqrt
from primeCheckII import primes
from memoise import Memoise

@Memoise
def findFactors(x):
    if x == 1:
        return([])
    X = x
    for p in primes(2,int(sqrt(X))+1):
        if not (X%p):
            X //= p
            return([p]+findFactors(X))
    return([X])
