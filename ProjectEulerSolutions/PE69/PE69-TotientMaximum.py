# PROJECT EULER PROBLEM 69 - Totient Maximum


from findDivisorsII import findDivisors
from findFactorsII import findFactors
from memoise import Memoise
import primeCheckII

@Memoise
def countFractions(N):
    s = N-1
    if not primeCheckII.PrimeCheck(N):    
        D = findDivisors(N,False,False)
        s -= sum([countFractions(d) for d in D])
    return(s)


max_n = 1000000
biggest = [0,0]
for n in range(max_n,1,-1):
    if n%1000 == 0:
        print(n)
    phi = countFractions(n)
    n_over_phi = n/phi
    if n_over_phi > biggest[1]:
        biggest[0] = n
        biggest[1] = n_over_phi

print(biggest)

