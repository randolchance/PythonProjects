# PROJECT EULER PROBLEM 203 - Squarefree Binomial Coefficients

from math import ceil
from combinationsII import nCr
from findFactorsII import findFactors
import primeCheckII

def isSquarefree(x):
    if x == 1:
        return(True)
    for p in primeCheckII.primes():
        p2 = p**2
        if p2 > x:
            return(True)
        elif x%p2 == 0:
            return(False)
        

ROWS = 51

squarefree_list = [1]
total = 1
for n in range(1,ROWS):
    max_r = ceil((n+1)/2)
    for r in range(max_r):
        N = nCr(n,r)
        if N == 1: continue
        G = findFactors(N)
        if not all([G[i] not in G[i+1:] for i in range(len(G))]):
            continue
        if N in squarefree_list: continue
        #print(N)
        squarefree_list.append(N)
        total += N
                
print(total)
    
