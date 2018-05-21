# PROJECT EULER PROBLEM 401 - Sum of Squares of Divisors

from collections import Counter
from math import sqrt

from primeCheck import primes
from primeCheck import isPrime
"""
def isPrime(x):
    if x == 2:
        return(True)
    if x == 1 or x%2 == 0 or x == 0:
        return(False)
    p = True
    i = 3
    while i <= int(sqrt(x)):
        if isPrime(i):
            p = p and (x%i != 0)
        i += 2
    return(p)

def primes(i=2,f=-1):
    while f == -1 or i < f:
        if isPrime(i):
            yield(i)
        i += (i%2!=0 and i!=1) + 1
"""        

# Takes a list of a range of indices and returns a list of lists of all
# possible combinations
# WIP: Better would likely be to also pass the list of factors, and instead
# of iterating z in newList to see if a new combo already exists using Counter(),
# calculate if the index products are the same. This has the advantage of
# eliminating unique index lists that result in duplicate products
def combinations(factors):
    if len(factors) == 0:
        yield([])
    else:
        divisors  = [1]+list(sorted(set([x for x in factors])))
        iList = [[x] for x in range(len(factors))]
        oldList = [x for x in iList]
        for r in range(len(factors)):
            newList = []
            for x in range(len(iList)):
                for y in oldList:
                    if iList[x][0] not in y:
                        a = iList[x]+y
                        A = 1
                        for i in a:
                            A *= factors[i]
                        notDupe = True
                        for z in newList:
                            Z = 1
                            for i in z:
                                Z *= factors[i]
                            if A == Z:
                                notDupe = False
                                break
                        if notDupe:
                            newList.append(a)
                            divisors.append(A)
            
            oldList = [x for x in newList]
        divisors.sort()
        for d in divisors:
            yield(d)

def findFactors(x):
    X = x
    factor_list = []
    if X < 0:
        factor_list.append(-1)
        X *= -1
    while X > 1:
        max_X = int(sqrt(X))
        for i in primes(2,max_X+1):
            if X%i == 0:
                factor_list.append(i)
                X = int(X/i)
                break
            if i >= max_X:
                factor_list.append(X)
                X = 1
                break
        if isPrime(X):
            factor_list.append(X)
            X = 1

    return(factor_list)

mod_val = 10**9
max_val = 10**15

test = [2,2,2,2,2,3,3,3,5,5,7,7,7,7,11,13,13]
test2 = [2,2,2,2,2,2,3,5,5,5,5,7,7,11,13,17,101,2551]
number = 288 
result = []
#for i in range(number+1):
divisor_list = []
factor_list = findFactors(number)
for x in combinations(factor_list):
    divisor_list.append(x)
print(factor_list,divisor_list)
"""    
    for i in x:
        X = 1
        for j in i:
            X *= test[j]
            if X not in result:
                result.append(X)
                result.sort()
print(result)
"""
