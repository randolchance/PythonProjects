# PROJECT EULER PROBLEM 77 - Prime Summations

from memoiseII import Memoise
import primeCheckII as PC

@Memoise
def findSums(N,n_0, count_self=True):
    if count_self and PC.PrimeCheck(N) and N <= n_0:
        yield(1)
    for n in PC.primes(2,n_0+1):
        dn = N-n
        if dn > 1:
            yield(sum([s for s in findSums(dn,min([dn,n]))]))


target_count = 5000

n = 2
while True:
    count = 0
    for s in findSums(n,n,False):
        count += s
    print(n,count)
    if count > target_count:
        break
    n += 1

print(n)
    
