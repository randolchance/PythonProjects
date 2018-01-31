from math import sqrt

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
    if f == -1 or i < f:
        while True:
            if isPrime(i):
                yield(i)
            i += (i%2!=0 and i!=1)+1
            if f != -1 and i >= f:
                break

max_prime = 10000000
with open("primes.txt",'r+') as file:
    prime_list = file.readlines()
    if len(prime_list) <= 2:
        start_prime = 2
    else:
        start_prime = int(prime_list[len(prime_list)-2].rstrip("\n"))
    for p in primes(start_prime,max_prime):
        file.write(str(p) + "\n")
