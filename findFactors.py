from math import sqrt

from primeCheck import primes

def findFactors(x):
    X = x
    results = []
    while True:
        X_max = int(sqrt(X))
        for p in primes(2,X_max+1):
            divided = not (X%p)
            if divided:
                X /= p
                results.append(p)
                break
        if not divided:
            results.append(int(X))
            break
    return(results)

