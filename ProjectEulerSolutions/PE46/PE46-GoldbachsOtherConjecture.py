# PROJECT EULER PROBLEM 46 - Goldbach's Other Conjecture

from math import sqrt
import primeCheckII

def oddComposite():
    x = 9
    yield(x)
    while True:
        x += 2
        if primeCheckII.PrimeCheck(x):
            continue
        yield(x)


for x in oddComposite():
    if not any([sqrt((x-p)//2)%1==0 for p in primeCheckII.primes(3,x)]):
        print(x)
        break
    #print(x)

