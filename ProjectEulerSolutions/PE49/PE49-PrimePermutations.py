# PROJECT EULER PROBLEM 49 - Prime Permutations

import primeCheckII
from permutations import permutation
from collections import Counter

PRIME_LENGTH = 4

def findSpecialPrimes():
    checked_list = []
    for prime in primeCheckII.primes(1000,10000):
        #print(prime)
        for p in permutation([x for x in range(len(str(prime)))],len(str(prime))):
            s = [str(prime)[x] for x in p]
            next_prime = int("".join(s))
            if len(str(next_prime)) < PRIME_LENGTH or next_prime <= prime:
                continue
            if primeCheckII.PrimeCheck(next_prime):
                d_prime = next_prime - prime
                last_prime = next_prime + d_prime
                if len(str(last_prime)) != PRIME_LENGTH:
                    continue
                if primeCheckII.PrimeCheck(last_prime):
                    if Counter([s for s in str(last_prime)]) == Counter(s):
                        if prime not in checked_list:
                            checked_list.append(prime)
                            yield([prime,next_prime,last_prime])


for primes in findSpecialPrimes():
    prime_str = ''
    for prime in primes:
        prime_str += str(prime)
    print(prime_str)

