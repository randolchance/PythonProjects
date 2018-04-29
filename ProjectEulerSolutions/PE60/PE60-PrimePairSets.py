"""
PROJECT EULER PROBLEM 60 - Prime Pair Sets
The primes 3, 7, 109, and 673, are quite remarkable. By taking
any two primes and concatenating them in any order the result
will always be prime. For example, taking 7 and 109, both 7109
and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two
primes concatenate to produce another prime.
"""
import permutations
import primeCheckII

def primePairSets(a_0,b_0,c_0,d_0,e_0):
    for a in primeCheckII.primes(a_0):
        for b in primeCheckII.primes(b_0,a+1):
            for c in primeCheckII.primes(c_0,b+1):
                for d in primeCheckII.primes(d_0,c+1):
                    for e in primeCheckII.primes(e_0,d+1):
                        primes_list = [a,b,c,d,e]
                        i_list = [x for x in range(len(primes_list))]
                        p_list = permutations.permutation(i_list,2)
                        allPrime = True
                        for i in p_list:
                            prime_str = ""
                            for x in i:
                                prime_str += str(primes_list[x])
                            allPrime = allPrime and primeCheckII.PrimeCheck(int(prime_str))
                        if allPrime:
                            return(primes_list)

a_0 = 673
b_0 = 110
c_0 = 109
d_0 = 7
e_0 = 3
result = primePairSets(a_0,b_0,c_0,d_0,e_0)
print(result)
total = 0
for x in result:
    total += x
print(total)
