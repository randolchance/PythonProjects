from math import sqrt
from primeCheckII import primes
from memoise import Memoise

@Memoise
def findFactors(x):
    X = x
    results = []
    while True:
        X_max = int(sqrt(X))
        divided = False
        for p in primes(2,X_max+1):
            divided = not (X%p)
            if divided:
                X /= p
                results.append(p)
                break
        if not divided:
            if X > 1:
                results.append(int(X))
            break
    return(results)

