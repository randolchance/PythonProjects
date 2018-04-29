"""
PROJECT EULER PROBLEM 183 - Maximum Product of Parts
Let N be a positive integer and let N be split into k equal parts,
r = N/k, so that N = r + r + ... + r.

Let P be the product of these parts, P = r × r × ... × r = rk.

For example, if 11 is split into five equal parts,
11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven
into four equal parts which leads to Pmax = (11/4)4; that is,
M(11) = 14641/256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three
equal parts, so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N
if M(N) is a terminating decimal.

For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

Find ΣD(N) for 5 ≤ N ≤ 10000.
"""
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
# 48861552 CORRECT
