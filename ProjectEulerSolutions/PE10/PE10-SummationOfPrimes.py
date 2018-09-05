# PROJECT EULER PROBLEM 10 - Summation of Primes


from primeCheckII import primes

max_prime = 2000000
total = 0
for p in primes(2,max_prime):
    total += p

print(total)

