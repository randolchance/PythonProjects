# PROJECT EULER PROBLEM 183 - Maximum Product of Parts
from math import sqrt
from primeCheckII import primes

def getFactors(x):
    X = x
    #factor_list = []
    while True:
        success = False
        max_p = int(sqrt(X))
        for p in primes(2,max_p+1):
            if X%p == 0:
                success = True
                X /= p
                yield(p)
                break
        if not success:
            yield(int(X))
            break
    #return(factor_list)


Nstart = 5
Nend = 10000
SumD = 0
K = 1
K_list = []
for N in range(Nstart, Nend+1):
    result = K
    for k in range(K,N):
        Q = ((k/(k+1))**k) * (N/(k+1))
        if Q < 1:
            result = k
            break
    if result > K:
        K = result
        K_list = [x for x in getFactors(K) if x in [p for p in primes(3,K+1) if p != 5]]
    D = -N
    M = N
    for factor in K_list:
        if M%factor != 0:
            D = N
            break
        else:
            M /= factor
    #print(N,K,D,K_list)
    SumD += D
print(SumD)
