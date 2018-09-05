# PROJECT EULER PROBLEM 47 - Distinct Primes Factors

import primeCheckII
from memoise import Memoise

@Memoise
def findPrimeFactors(x,n):
    prime_factors = {}
    X = x
    for p in primeCheckII.primes():
        if p > X:
            break
        while X%p == 0:
            X /= p
            if p not in prime_factors:
                prime_factors[p] = 1
            else:
                prime_factors[p] += 1
        if len(prime_factors) > n:
            return(False)
        if X == 1:
            break
    if len(prime_factors) != n:
        return(False)
    #print(x,prime_factors)
    return(prime_factors)


N_FACTORS = 4

x = 1
while True:
    if all([findPrimeFactors(x+z,N_FACTORS) for z in range(N_FACTORS)]):
        print(x)
        break
    x += 1

