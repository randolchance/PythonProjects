from math import sqrt
from primeCheck import primes


max_prime = 10000000
with open("primes.txt",'r+') as file:
    prime_list = file.readlines()
    if len(prime_list) <= 2:
        start_prime = 2
    else:
        start_prime = int(prime_list[len(prime_list)-2].rstrip("\n"))
    for p in primes(start_prime,max_prime):
        file.write(str(p) + "\n")
