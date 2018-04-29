"""
PROJECT EULER PROBLEM 141 - Investigating Progressive Numbers, n,
Which Are Also Square

A positive integer, n, is divided by d and the quotient and remainder
are q and r respectively. In addition d, q, and r are consecutive
positive integer terms in a geometric sequence, but not necessarily
in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can
also be seen that 4, 6, 9 are consecutive terms in a geometric
sequence (common ratio 3/2).

We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102^2, happen to also
be perfect squares.

The sum of all progressive perfect squares below one hundred thousand
is 124657.

Find the sum of all progressive perfect squares below one trillion (10^12).
"""

from math import sqrt
from primeCheckII import primes
from collections import Counter

def getFactors(x):
    X = x
    factor_list = []
    while True:
        success = False
        max_p = int(sqrt(X))
        for p in primes(2,max_p+1):
            if X%p == 0:
                success = True
                X /= p
                factor_list.append(p)
                break
        if not success:
            factor_list.append(int(X))
            break
    return(factor_list)


#max_nsquared = 100000
#max_n = int(sqrt(max_nsquared))
max_n = 1000000
max_nsquared = max_n**2
max_p = int(max_n**(2/3))
total = 0
for p in range(2,max_p):
    for m in range(1,p):
        if m > 1:
            m_list = Counter(getFactors(m))
            dupe = False
            for key in m_list.keys():
                if (p/key)%1 == 0:
                    dupe = True
                    break
            if dupe:
                continue
        #print(p,m)
        k = p/m
        Q = 0
        while True:
            Q += 1
            if sqrt(m)%1 == 0:
                R = int(Q*m**(3/2))
                nsquared = Q**2*p**3 + R
                special = True
            else:
                R = int(Q*m**2)
                nsquared = Q**2*m*p**3 + R
                special = False
            if nsquared >= max_nsquared:
                break
            n = sqrt(nsquared)
            if n%1 == 0:
                n = int(n)
                d = int(k*R)
                q = int(k**2*R)
                n = int(sqrt(nsquared))
                print(p,m,R,d,q,n,int(nsquared),special)
                
                total += nsquared
print(total)
# 797774730732 WRONG
# 935281685159 WRONG
