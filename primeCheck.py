from math import sqrt

def isPrime(x,prime_list=[]):
    if x == 2:
        return(True)
    if x == 1 or x%2 == 0 or x == 0:
        return(False)
    max_x = int(sqrt(x))
    
    def _noList(j=3):
        while j <= max_x:
            if isPrime(j):
                if x%j == 0:
                    return(False)
            j += 2
        return(True)

    start_j = 3
    if prime_list:
        if x >= prime_list[0]:
            for i in prime_list:
                if x == i or i > max_x:
                    return(True)
                elif x%i == 0:
                    return(False)
                else:
                    start_j = i
    else:
        pass
    return(_noList(start_j))
        

def primes(k=2,f=-1):
    prime_list = []
    i = 2
    while f == -1 or i < f:
        if isPrime(i,prime_list):
            if i >= k:
                yield(i)
            prime_list.append(i)
        i += (i%2!=0 and i!=1) + 1

