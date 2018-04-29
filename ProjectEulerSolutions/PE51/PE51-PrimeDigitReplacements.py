"""
PROJECT EULER PROBLEM 51 - Prime Digit Replacements
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

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
"""
def primes(i=2,f=-1):
    if f == -1 or i < f:
        while True:
            if isPrime(i):
                yield(i)
            i += (i%2!=0 and i!=1)+1
            if f != -1 and i >= f:
                break

def isPrime(x):
    with open("primes.txt") as file:
        for line in file:
            p = file.readline()
            prime = int(p.rstrip("\n"))
            if prime > x:
                return(False)
            if prime == x:
                return(True)

def primes(i=2,f=-1):
    with open("primes.txt") as file:
        for line in file:
            p = file.readline()
            prime = int(p.rstrip("\n"))
            if prime < i:
                continue
            elif prime >= f and f != -1:
                break
            else:
                yield(prime)
"""

class Primes:
    def __init__(self, start_prime):
        self.prime_list = []
        self.start_prime = start_prime
        with open("primes.txt") as file:
            for line in file:
                p = line
                prime = int(p.rstrip("\n"))
                if prime < self.start_prime:
                    continue
                self.prime_list.append(prime)

    def getList(self):
        return(self.prime_list)


def bitList(x):
    # NOTE: The additional -1 in the range is to omit masks with all 1s
    for i in range(1,(2<<(x-1))-1):
        out = str(bin(i)).lstrip("0b")
        while len(out) < x:
            out = "0"+out
        yield(out)


def findPrimeFamily(start_prime,family_size):
    result = []
    PrimeList = Primes(start_prime)
    for p in PrimeList.getList():
        print(p)
        str_p = str(p)
        for bitMask in bitList(len(str_p)):
            prime_family = []
            if bitMask[0] == "1":
                i_0 = 1
            else:
                i_0 = 0
            for i in range(i_0,10):
                new_str_p = ""
                for s in range(len(str_p)):
                    if bitMask[s] == "1":
                        new_str_p += str(i)
                    else:
                        new_str_p += str_p[s]
                new_p = int(new_str_p)
                if new_p in PrimeList.getList():
                    prime_family.append(new_p)
            if len(prime_family) >= family_size:
                if prime_family not in result:
                    result.append(prime_family)
                    print(prime_family)
                return(result)




# ANSWER: -=121313=- (222323, 323333, 424343, 525353, 626363, 828383, 929393)
family_size = 8
print(findPrimeFamily(106871,family_size))
