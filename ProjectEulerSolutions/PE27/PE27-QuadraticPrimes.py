# PROJECT EULER PROBLEM 27 - Quadratic Primes


from primeCheckII import IsPrime

primeCheck = IsPrime()

def f(n,a,b):
    return(n**2+a*n+b)


biggest_prime_data = []
for a in range(-999,1000):
    for b in range(-1000,1001):
        prime_list = []
        allPrimes = True
        n = 0
        while allPrimes:
            y = f(n,a,b)
            if y <=1:
                allPrimes = False
            else:
                if primeCheck(y):
                    prime_list.append(y)
                else:
                    allPrimes = False
            n += 1
        if not biggest_prime_data:
            biggest_prime_data = [a,b,prime_list]
        else:
            if len(prime_list) > len(biggest_prime_data[2]):
                biggest_prime_data = [a,b,prime_list]
        

print(biggest_prime_data)
print(len(biggest_prime_data[2]))
print(biggest_prime_data[0]*biggest_prime_data[1])

